from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def say_hi():
    print("Hi 👋")

def say_goodbye():
    print("Goodbye 👋")

with DAG(
    dag_id='simple_greeting_dag',
    start_date=datetime(2025, 5, 24),
    schedule_interval='* * * * *',  # every minute
    catchup=False,
) as dag:
    hi = PythonOperator(task_id="say_hi", python_callable=say_hi)
    bye = PythonOperator(task_id="say_goodbye", python_callable=say_goodbye)
    hi >> bye

