from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.utils.dates import days_ago

with DAG(
    dag_id='kubernetes_sleep_dag',
    schedule=None,
    start_date=days_ago(1),
    catchup=False,
    tags=['example'],
) as dag:

    sleep_task = KubernetesPodOperator(
        task_id="sleep-task",
        name="sleep-task",
        namespace="airflow",  # match your namespace
        image="busybox",
        cmds=["/bin/sh", "-c"],
        arguments=["echo Starting sleep; sleep 30; echo Finished"],
        get_logs=True,
        is_delete_operator_pod=True,
    )

    sleep_task
