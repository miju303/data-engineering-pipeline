📊 Sales Data Engineering Pipeline
An end-to-end data pipeline that ingests raw retail sales data, cleans and transforms it, loads it into a PostgreSQL data warehouse, and automates the entire workflow on a daily schedule using Apache Airflow.
Overview
This project simulates a real-world data engineering workflow — taking messy, raw data from a source file and turning it into clean, structured, queryable data ready for analytics, with the whole process running automatically without manual intervention.
Architecture
Code
Pipeline Stages
1. Ingestion
Raw sales order data (51,000+ records, 21 columns) is read from a CSV file using pandas.
2. Transformation
Converted sales from text to numeric (float), handling comma-formatted values
Parsed inconsistent date formats in order_date and ship_date into proper datetime objects
Validated data types across all columns before loading
3. Loading
Cleaned data is loaded into a PostgreSQL database (salesdb) into an orders table using SQLAlchemy.
4. Orchestration & Automation
The entire pipeline (ingest → transform → load) is wrapped in an Apache Airflow DAG, scheduled to run automatically once per day, with full logging and failure tracking through the Airflow UI.
Tech Stack
Layer
Tool
Language
Python 3.13
Data Processing
pandas
Database
PostgreSQL 17
DB Connector
SQLAlchemy, psycopg2
Orchestration
Apache Airflow 3.2
Environment
WSL (Ubuntu) on Windows
Editor
VS Code
Project Structure
Code
Key Challenges Solved
Mixed data types: Source columns intended as numbers were stored as text with comma separators
Inconsistent date formats: Order/ship dates appeared in multiple formats within the same column, requiring flexible parsing
Cross-environment networking: Airflow (running in WSL/Linux) needed to reach PostgreSQL (running on Windows) across the WSL network boundary — resolved by identifying the correct gateway IP and configuring PostgreSQL + Windows Firewall to accept the connection
What I Learned
This was a hands-on, from-scratch build covering the full data engineering lifecycle: environment setup, data ingestion, cleaning/transformation, database loading, and workflow orchestration — including debugging real infrastructure issues like cross-network database connectivity and firewall configuration.
Future Improvements
[ ] Add a visualization/analytics layer (Streamlit or Power BI dashboard)
[ ] Add automated data quality checks
[ ] Containerize the pipeline with Docker
[ ] Add unit tests for transformation logic