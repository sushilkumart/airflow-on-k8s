from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.utils.dates import days_ago

with DAG(
    dag_id="kpo_in_podman",
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False,
) as dag:

    k8s_task = KubernetesPodOperator(
        namespace='default',
        image="python:3.9-slim",
        cmds=["python", "-c"],
        arguments=["print('Hello from K8s pod!')"],
        labels={"foo": "bar"},
        name="example-pod",
        task_id="run_pod_in_k8s",
        get_logs=True,
        is_delete_operator_pod=True,
        config_file="/root/.kube/config"
    )
