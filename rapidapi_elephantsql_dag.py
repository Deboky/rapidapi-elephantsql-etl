from common.utils import *
from rapidapi_elephantsql_etl import rapidapi_elephantsql_etl



# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['xyz_email@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 4, 20),
    'catchup': False
}

# Define the DAG
dag = DAG(
    'etl_rapidapi_to_elephantsql',
    default_args=default_args,
    description='Daily ETL from RapidAPI to ElephantSQL',
    schedule_interval='@daily',  # Run once a day
)

# Define the task using a PythonOperator
etl_task = PythonOperator(
    task_id='run_etl',
    python_callable=rapidapi_elephantsql_etl,
    dag=dag,
)

# We can add more tasks using similar pattern

# etl_task can be set as the starting point
etl_task

