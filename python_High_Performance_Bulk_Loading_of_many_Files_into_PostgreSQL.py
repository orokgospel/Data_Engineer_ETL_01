give me a brief description and title of what this code does:
from sqlalchemy import create_engine
import pandas as pd
import psycopg2
import io

# ==============================
# PostgreSQL Connection Details
# ==============================

pg_username = 'postgres'
pg_password = 'Jesus200'
pg_host = 'localhost'
pg_port = '5433'
pg_database = 'training_db'

engine = create_engine(
    f'postgresql+psycopg2://{pg_username}:{pg_password}@{pg_host}:{pg_port}/{pg_database}'
)

# ==============================
# File Paths
# ==============================

files = [
    r'C:\Users\USER\Documents\file1.csv',
    r'C:\Users\USER\Documents\file2.csv',
    r'C:\Users\USER\Documents\file3.csv',
    r'C:\Users\USER\Documents\file4.csv'
]

table_name = 'stage_table'

# ==============================
# Read & Combine Files Safely
# ==============================

dfs = []

for file in files:
    df = pd.read_csv(
        file,
        dtype=str,
        skip_blank_lines=True
    )

    # Remove completely empty columns
    df = df.dropna(axis=1, how='all')

    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)

print("Final shape:", combined_df.shape)

# ==============================
# Create Table (Replace if Exists)
# ==============================

combined_df.head(0).to_sql(
    table_name,
    engine,
    if_exists='replace',
    index=False
)

# ==============================
# FAST INSERT USING COPY
# ==============================

conn = engine.raw_connection()
cur = conn.cursor()

output = io.StringIO()
combined_df.to_csv(output, sep='\t', header=False, index=False)
output.seek(0)

cur.copy_from(output, table_name, null="")

conn.commit()
cur.close()
conn.close()

print(f"✅ Table '{table_name}' loaded successfully using COPY (fast mode).")