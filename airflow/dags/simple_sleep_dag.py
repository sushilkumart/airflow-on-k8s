from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import time

def sleep_task():
    print("Sleeping for 30 seconds...")
    time.sleep(300)
    print("Done sleeping.")

with DAG(
    dag_id="simple_sleep_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,  # Run manually
    catchup=False,
    tags=["example"],
) as dag:

    sleep = PythonOperator(
        task_id="sleep_30_seconds",
        python_callable=sleep_task,
    )
