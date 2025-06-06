from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
}

with DAG(
    dag_id='kubernetes_operator_simple_dag',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=['example', 'kubernetes'],
) as dag:

    sleep_task = KubernetesPodOperator(
        task_id="sleep_task",
        name="sleep-pod",
        namespace="airflow",  # Ensure this matches your Helm release namespace
        image="busybox",
        cmds=["sh", "-c", "echo 'Sleeping for 30s...'; sleep 30; echo 'Done.'"],
        get_logs=True,
        is_delete_operator_pod=True,
    )
