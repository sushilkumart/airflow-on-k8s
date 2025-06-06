from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def say_hello():
    print("Hello from Airflow!")

with DAG(
    dag_id="hello_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@once",  
    catchup=False
) as dag:
    hello_task = PythonOperator(
        task_id="say_hello",
        python_callable=say_hello
    )
