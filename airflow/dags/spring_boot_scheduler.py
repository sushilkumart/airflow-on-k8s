from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime

with DAG(
    dag_id='spring_boot_scheduler',
    start_date=datetime(2025, 6, 9),
    schedule_interval=None,
    catchup=False
) as dag:
    run_spring_boot = KubernetesPodOperator(
        task_id='run_spring_boot_task',
        name='spring-boot-pod',
        namespace='default',
        image='sktaskar/airflow1:latest',
        cmds=["java", "-jar", "app.jar"],
        get_logs=True
    )
