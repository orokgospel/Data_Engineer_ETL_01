import pandas as pd
from sqlalchemy import create_engine, text
import math
import os

# ================================
# PostgreSQL Connection Settings
# ================================
pg_username = 'postgres'
pg_password = 'Jesus200#'
pg_host     = "localhost"
pg_port     = '5433'
pg_database = 'training_db'

engine = create_engine(
    f'postgresql+psycopg2://{pg_username}:{pg_password}@{pg_host}:{pg_port}/{pg_database}'
)

# =======================================
# Export settings
# =======================================
TABLE_NAME  = "public.individual_acct"
BATCH_SIZE  = 1_000_000
START_BATCH = 3   # 👈 CHANGE THIS IF NEEDED
EXPORT_PATH = "./exports"

os.makedirs(EXPORT_PATH, exist_ok=True)

# =======================================
# Get total record count
# =======================================
with engine.connect() as conn:
    total_records = conn.execute(
        text(f"SELECT COUNT(*) FROM {TABLE_NAME}")
    ).scalar()

print(f"Total Records: {total_records}")

num_batches = math.ceil(total_records / BATCH_SIZE)

print(f"Total Batches: {num_batches}")
print(f"Forcing start from Batch: {START_BATCH}")

# =======================================
# Start Offset Calculation
# =======================================
offset = (START_BATCH - 1) * BATCH_SIZE
batch_number = START_BATCH

try:
    while offset < total_records:

        print(f"Processing Batch {batch_number} | OFFSET {offset}")

        query = f"""
            SELECT 
                account_id,
                "Account Name",
                customer,
                sta_code,
                working_balance,
                currency,
                street,
                customer_type,
                "customer status description",
                address,
                town_country,
                phone_1,
                sms_1,
                date_of_birth::text AS date_of_birth,
                email_1,
                last_transaction_year_month,
                last_transaction_date::text AS last_transaction_date,
                last_transaction_time::text AS last_transaction_time
            FROM {TABLE_NAME}
            ORDER BY account_id
            LIMIT {BATCH_SIZE}
            OFFSET {offset}
        """

        df = pd.read_sql(query, engine, parse_dates=False)

        if df.empty:
            print("No more records found.")
            break

        file_name = f"{EXPORT_PATH}/individual_acct_batch_{batch_number}.csv"

        df.to_csv(file_name, index=False)

        print(f"Saved: {file_name}")
        print("----------------------------------")

        offset += BATCH_SIZE
        batch_number += 1

    print("Export Completed Successfully!")

except KeyboardInterrupt:
    print("Process stopped manually.")

finally:
    engine.dispose()
    print("Database connection closed.")