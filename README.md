# Gospel_ETL_&_ELT_for_Data-Engineering

# End-to-End Banking ETL Pipeline with Monitoring & Alerting

This project demonstrates a production-grade data engineering pipeline
that extracts, transforms, and loads banking transaction data into a PostgreSQL data warehouse,
with monitoring, alerting, and batch processing capabilities.


This is my ETL as well as the logging Python Project for Data Engineering.

In this project I did the following:
-Run the ETL process
-Extract bank and market cap data from the JSON file bank_market_cap.json
-Transform the market cap currency using the exchange rate data
-Load the transformed data into a seperate CSV

Also went ahead to use the learning experience and project to carry out an ETL project that performs the following:
- Read or collect inputted batch pumping parameters of petroleum product from source station or depot.
- Transform the collected data.
- Save the transformed data in a ready-to-load csv format which data engineers can use to load into an RDBMS or Data Analyst/Scientist can use for Analysis.



<img width="1200" height="693" alt="image" src="https://github.com/user-attachments/assets/ff134da5-ff65-48c4-8b2b-d530ebc70032" />



# Tech Stack
1. Python
2. PostgreSQL
3. Apache Airflow
4. Docker
6. SQL
7. Pandas
8. Flink
9. Iceberg
10. Trino

# Data Sources
Custom made Banking transaction datasets
JSON market data
Pump station batch data


# Pipeline Workflow (Step-by-Step)
1. Extract data from source systems (PostgreSQL / JSON)
2. Transform data (cleaning, currency conversion, formatting)
3. Load into staging tables
4. Move into warehouse tables
5. Run monitoring scripts for locks & performance
6. Trigger alerts via email (Airflow DAG)
