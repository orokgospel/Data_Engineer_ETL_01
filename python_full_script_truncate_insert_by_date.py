import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "port": "5433",
    "database": "training_db",
    "user": "postgres",
    "password": "Jesus200#"
}

def truncate_and_insert():
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        print("✅ Connection successful")

        cursor.execute("TRUNCATE TABLE customers_stage;")

        insert_query = """
            INSERT INTO customers_stage
            SELECT customer_id,
            full_name,email,
            phone::BIGINT,
            created_at
            FROM customers
            LIMIT 10;
        """

        cursor.execute(insert_query)
        conn.commit()
        print("✅ Data inserted successfully")
        cursor.close()
        conn.close()

        print("🔒 Connection closed")
        print("Job done")


if __name__ == "__main__":
    truncate_and_insert()
