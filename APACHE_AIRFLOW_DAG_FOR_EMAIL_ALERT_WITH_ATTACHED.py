from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
from sqlalchemy import create_engine
from sqlalchemy.engine import URL


# CONFIG
SENDER_EMAIL = "orokgospel@gmail.com"
SENDER_PASSWORD = "ywuk xdzg citw dtgb"
RECEIVER_EMAIL = "orokgospel@gmail.com"

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

# ✅ Airflow-safe path (VERY IMPORTANT)
OUTPUT_FILE = "/opt/airflow/dags/transactions_export.xlsx"

MAX_ROWS_PER_SHEET = 1_000_000


# DATABASE CONNECTION
connection_url = URL.create(
    "postgresql+psycopg2",
    username="postgres",
    password="Jesus200#",
    host="host.docker.internal",   # 🔥 IMPORTANT if using Docker
    port=5433,
    database="training_db"
)

engine = create_engine(connection_url)

QUERY = "SELECT * FROM customers LIMIT 200"


# TASK 1: EXTRACT + EXPORT
def extract_customers():
    df = pd.read_sql(QUERY, engine)

    if df.empty:
        raise ValueError("No data found in customers table")

    with pd.ExcelWriter(OUTPUT_FILE, engine="xlsxwriter") as writer:
        total_rows = len(df)
        sheet_number = 1

        for start in range(0, total_rows, MAX_ROWS_PER_SHEET):
            end = start + MAX_ROWS_PER_SHEET
            df_chunk = df.iloc[start:end]

            sheet_name = f"Sheet{sheet_number}"
            df_chunk.to_excel(writer, sheet_name=sheet_name, index=False)

            sheet_number += 1

    print(f"File saved at {OUTPUT_FILE}")

# TASK 2: SEND EMAIL
def send_email():
    if not os.path.exists(OUTPUT_FILE):
        raise FileNotFoundError("Excel file not found.")

    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = "Daily Customers Report"

    body = "Hi,\n\nPlease find attached the daily customers report.\n\nRegards."
    msg.attach(MIMEText(body, 'plain'))

    # Attach file
    with open(OUTPUT_FILE, 'rb') as f:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename={os.path.basename(OUTPUT_FILE)}'
        )
        msg.attach(part)

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())

    print("Email sent successfully")

# TASK 3: CLEANUP
# =========================
def cleanup_file():
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
        print(f"Deleted file: {OUTPUT_FILE}")
    else:
        print("No file found to delete.")

# DAG DEFINITION
default_args = {
    'owner': 'Gospel Orok',
    'depends_on_past': False,
    'retries': 1,
}

with DAG(
    dag_id='ppl_etl_customers_to_email',
    default_args=default_args,
    description='Extract customers and send as Excel via email',
    schedule='0 8 * * *',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['etl', 'email'],
) as dag:

    task_extract = PythonOperator(
        task_id='extract_customers',
        python_callable=extract_customers
    )

    task_email = PythonOperator(
        task_id='send_email',
        python_callable=send_email
    )
    task_cleanup = PythonOperator(
        task_id='cleanup_file',
        python_callable=cleanup_file
    )

    task_extract >> task_email>> task_cleanup
