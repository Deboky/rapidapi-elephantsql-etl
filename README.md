## RapidAPI to ElephantSQL ETL Pipeline

### Overview
This ETL pipeline automates the data flow from RapidAPI to an ElephantSQL database, optimized for daily updates via Apache Airflow. The goal of this project is to reduce the cost as much as possible. Here, I have used open source [API](https://rapidapi.com/hub)

### Technological Stack
This project leverages various technologies across its ETL processes:

- **Python**: Used for scripting the ETL pipeline, providing flexibility and powerful data manipulation capabilities.
- **Apache Airflow**: Serves as the orchestrator for scheduling, monitoring, and managing the ETL workflow.
- **RapidAPI**: Source API platform from which data is extracted.
- **ElephantSQL**: PostgreSQL as a service that acts as the data warehousing solution.
- **Pandas**: Used within Python scripts for data cleaning, transformation, and analysis.

### Data Pipeline Steps

#### Extract
- **Sources**: Data is sourced from APIs. Usually for other apis there are aunthentication techniques which is needs to be added into the config files and must not be exposed as there are senstive information.
- **Tools**: Utilizes standard HTTP requests for data extraction.

#### Transform
- **Operations**: Cleansing errors, removing duplicates and data aggregation and filtering.
- **Tools**: Python is used for scripting transformation processes

#### Load
- **Destination**: Data is loaded into ElephantSQL, a PostgreSQL as a service.
- **Storage Options**: (which can be used for any company)
  - **Data Warehouse**: Central repository for CRM, API, and ERP data.
  - **Data Lake**: Stores structured and unstructured data.
  - **Database**: Managed by DBMS for structured data access.

#### End Users
Data Scientists, Analysts, and Business Analysts are the primary users, leveraging the data for advanced analytics and decision-making.

### Orchestration with Apache Airflow
- **Functionality**: Schedules and monitors the ETL tasks, ensuring reliability and timeliness of data updates.
- **Frequency**: Configured to run the pipeline daily.


For more information on Apache Airflow, visit the [Airflow Homepage](https://airflow.apache.org/).
