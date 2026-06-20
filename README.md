# Sales Data Engineering Pipeline

## Overview
This project ingests raw sales data, cleans it, loads it into PostgreSQL, and automates the pipeline using Apache Airflow.

## Pipeline Stages

**1. Ingestion**
Raw sales data is read from a CSV file using pandas.

**2. Transformation**
- Converted sales column from text to numeric
- Fixed inconsistent date formats
- Validated data types

**3. Loading**
Clean data is loaded into PostgreSQL using SQLAlchemy.

**4. Automation**
The pipeline runs daily, automated using Apache Airflow.

## Tech Stack
- Python (pandas, SQLAlchemy)
- PostgreSQL
- Apache Airflow
- VS Code

## What I Learned
This project covers the full data engineering lifecycle: ingestion, transformation, loading, and automation.

## Dashboard
An interactive Streamlit dashboard (`dashboard.py`) visualizes the cleaned sales data with:
- Key metrics (total sales, profit, orders, average order value)
- Sales by category and region
- Sales trend over time
- Top 10 products by sales
- Filterable by year and region

## Future Improvements
- [ ] Add data quality checks
- [ ] Containerize with Docker