import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "port": 5433,
    "database": "training_db",
    "user": "postgres",
    "password": "Jesus200#"
}

def call_procedure():
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        print("✅ Connection successful")

        # Call stored procedure
        # cursor.callproc("sp_update_account_balance")
        # conn.commit()
        cursor.execute("CALL sp_update_account_balance();")
        conn.commit()

        print("✅ Stored procedure executed successfully")
        cursor.close()
        conn.close()
        print("🔒 Connection closed")
        print("Job done")

if __name__ == "__main__":
    call_procedure()
