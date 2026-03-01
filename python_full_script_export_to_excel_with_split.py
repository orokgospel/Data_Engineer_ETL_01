# FULL SCRIPT – EXPORT TO EXCEL WITH SHEET SPLIT

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

MAX_ROWS_PER_SHEET = 1_000_000
OUTPUT_FILE = r"C:\Users\USER\OneDrive\Documentos\Python Scripts\transactions_export.xlsx"

connection_url = URL.create(
    "postgresql+psycopg2",
    username="postgres",
    password="Jesus200#",
    host="localhost",
    port=5433,
    database="training_db"
)

engine = create_engine(connection_url)
print('connection successfull')


def export_transactions_to_excel():
    df = pd.read_sql("SELECT * FROM customers LIMIT 2000000", engine)
    print('select done successfully')

    with pd.ExcelWriter(OUTPUT_FILE, engine="xlsxwriter") as writer:
        total_rows = len(df)
        sheet_number = 1

        for start in range(0, total_rows, MAX_ROWS_PER_SHEET):
            end = start + MAX_ROWS_PER_SHEET
            df_chunk = df.iloc[start:end]

            sheet_name = f"Sheet{sheet_number}"
            df_chunk.to_excel(writer, sheet_name=sheet_name, index=False)

            sheet_number += 1

    print("Transactions exported to Excel successfully")


if __name__ == "__main__":
    export_transactions_to_excel()