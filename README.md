# Modern Data Warehouse on AWS (ETL-Process)
This project was done in a data engineering bootcamp at SDA &amp; WeCloudData

## Project Overview
This project involves Analytical Data Engineering, focusing on ingesting data from various sources into the Snowflake data warehouse. The data undergoes transformation processes to prepare it for Business Intelligence (BI) usage. The BI tool Metabase connects to the data warehouse to generate diverse dashboards and reports.
![image](https://github.com/ghada6al/CapstoneProject-ETL-Process-/assets/74125257/07aedf13-4546-494b-a804-d9bf7319d112)

## About Data
### Data Background
The dataset originates from TPCDS, designed for database testing, with a focus on Retail Sales. It includes sales records from websites and catalogs, detailed inventory information for each item in every warehouse, and 15 dimensional tables containing valuable customer, warehouse, and item information.
![image](https://github.com/ghada6al/CapstoneProject-ETL-Process-/assets/74125257/e4d8e73a-7108-4d04-a893-c6e167a226b9)


### Dataset Split
- **RDS**: All tables, except for the inventory tables, are stored in a Postgres DB on AWS RDS, refreshed daily with the latest sales data.
- **S3 Bucket**: The inventory table is stored in an S3 bucket, with a new file containing the most recent data deposited daily.

## Business Requirements
### Metabase Requirements
- Determine top and bottom-performing items weekly based on sales amounts and quantities.
- Show items with low inventory levels weekly.
- Identify items with low stock levels, including their associated week and warehouse numbers, marked as "True".

## Project Infrastructure
- Cloud-based infrastructure:
  - Servers: AWS EC2 instances for Airbyte and Metabase.
  - Tools: Airbyte for data ingestion, Metabase for BI dashboards.
  - Cloud Data Warehouse: Snowflake for data storage and transformation.
  - AWS Lambda: Used to ingest data from S3 to Snowflake.

## Part One: Data Ingestion
- **Data Sources**: Postgres database (RDS) and S3 bucket.
- **Airbyte**: Connects to Postgres DB to transfer all tables to Snowflake. Also uses AWS Lambda to transfer the inventory.csv file from S3 to Snowflake.
- ![image](https://github.com/ghada6al/CapstoneProject-ETL-Process-/assets/74125257/23528b67-e846-438d-bebb-6bfd3cd437b6)


## Part Two: Data Transformation
- **Snowflake Data Warehouse**: Reshapes tables for desired format, including creating new fact tables and consolidating raw tables.
- ![image](https://github.com/ghada6al/CapstoneProject-ETL-Process-/assets/74125257/b43e95e6-02f4-48d3-94f1-8eaa4484ad14)


## Part Three: Data Analysis
- Establishes connection between Snowflake data warehouse and Metabase for dashboard and report creation.
- ![image](https://github.com/ghada6al/CapstoneProject-ETL-Process-/assets/74125257/7cfc9837-2ad8-442e-a745-3acc4b73275a)


