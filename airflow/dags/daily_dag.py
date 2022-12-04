import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {"owner": "airflow"}

with DAG(
        dag_id="daily_dag",
        start_date=datetime.datetime(2022, 9, 12),
        schedule_interval="00 23 * * *",
        default_args=default_args,
        catchup=False,
) as dag:
    daily_dag_start = BashOperator(
        task_id='daily_dag_start',
        bash_command='echo Load raw data into data lake on {{ ds }}',
    )

    load_into_ods_completed = BashOperator(
        task_id="load_into_ods_completed",
        bash_command='echo data in lake on {{ ds }} has been loaded into ods',
    )

daily_dag_start >> load_into_ods_completed
