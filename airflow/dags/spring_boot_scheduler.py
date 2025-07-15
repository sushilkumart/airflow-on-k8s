from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
}

with DAG(
    dag_id='spring_dag',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=['example', 'kubernetes'],
) as dag:

    airflow_task1 = KubernetesPodOperator(
        task_id="a1_task",
        name="a1-pod",
        namespace="airflow",  # Ensure this matches your Helm release namespace
        image="sktaskar/airflow1",
        get_logs=True,
        is_delete_operator_pod=True,
    )
    
    airflow_task2 = KubernetesPodOperator(
      task_id="a2_task",
      name="a2-pod",
      namespace="airflow",  # Ensure this matches your Helm release namespace
      image="sktaskar/airflow1",
      get_logs=True,
      execution_timeout=timedelta(minutes=1),
      is_delete_operator_pod=True,
    )
    
    airflow_task3 = KubernetesPodOperator(
      task_id="a3_task",
      name="a3-pod",
      namespace="airflow",  # Ensure this matches your Helm release namespace
      image="sktaskar/airflow1",
      get_logs=True,
      is_delete_operator_pod=True,
      trigger_rule="all_success"
    )
    
airflow_task1 >> airflow_task2 >> airflow_task3