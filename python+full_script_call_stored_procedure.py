import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "port": 5433,
    "database": "training_db",
    "user": "postgres",
    "password": "Jesus200#"
}

def call_procedure():
    conn = None
    cursor = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        print("✅ Connection successful")

        # Call stored procedure
        # cursor.callproc("sp_update_account_balance")
        # conn.commit()
        cursor.execute("CALL sp_update_account_balance();")
        conn.commit()

        print("✅ Stored procedure executed successfully")

    except Exception as e:
        print("❌ Error:", e)
        if conn:
            conn.rollback()
            print("🔄 Transaction rolled back")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("🔒 Connection closed")
        print("Job done")

if __name__ == "__main__":
    call_procedure()