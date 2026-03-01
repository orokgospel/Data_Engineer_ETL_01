import pandas as pd 
from sqlalchemy import create_engine 
from sqlalchemy.engine import URL
 
CSV_FILE = "C:/Users/USER/OneDrive/Documentos/Python Scripts/customers_export.csv" 
#EXCEL_FILE = r"C:\Users\USER\OneDrive\Documentos\Python Scripts\customers_export.xlsx"
TABLE_NAME = "customers_stage" 

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


def load_csv_to_postgres(): 
    df = pd.read_csv(CSV_FILE)
    #df = pd.read_excel(EXCEL_FILE, engine="openpyxl") 
       
    # Optional: clean column names (recommended)
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Automatically create table and load data
    df.to_sql( 
        name=TABLE_NAME, 
        con=engine, 
        if_exists="replace",  # change to append if needed or use "append" if table already exists
        index=False, 
        chunksize=5000 
    ) 
    print("CSV or excel data loaded into PostgreSQL successfully") 
if __name__ == "__main__": 
    load_csv_to_postgres() 