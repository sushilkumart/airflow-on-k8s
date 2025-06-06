from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

def test_task():
    print("Simple task works!")

with DAG("test_dag_simple1", start_date=days_ago(1), schedule_interval=None, catchup=False) as dag:
    task = PythonOperator(
        task_id="simple_task",
        python_callable=test_task
    )
