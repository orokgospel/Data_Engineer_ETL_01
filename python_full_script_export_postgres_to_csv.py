# FULL SCRIPT – EXPORT POSTGRES TABLE TO CSV

import psycopg2
import csv

DB_CONFIG = {
    "host": "localhost",
    "port": "5433",
    "database": "training_db",
    "user": "postgres",
    "password": "Jesus200#"
}

# ✅ Updated output path
OUTPUT_FILE = r"C:\Users\USER\OneDrive\Documentos\Python Scripts\customers_export.csv"
#OUTPUT_FILE = r"C:\Users\USER\OneDrive\Documentos\Python Scripts\customers_export.xlsx"

def export_table_to_csv():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        print('Connection to Postgres DB successful')

        query = "SELECT * FROM customers LIMIT 10;"
        cursor.execute(query)
        print('Select query successful')

        colnames = [desc[0] for desc in cursor.description]
        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(colnames)
            writer.writerows(cursor.fetchall())
        
        # Export to Excel
        # df.to_excel(
        #     OUTPUT_FILE,
        #     index=False,
        #     engine="openpyxl")


        print("✅ Customers exported successfully")
        print(f"📁 File saved to: {OUTPUT_FILE}")

    except Exception as e:
        print("❌ Error:", e)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
        print('Job done')

if __name__ == "__main__":
    export_table_to_csv()