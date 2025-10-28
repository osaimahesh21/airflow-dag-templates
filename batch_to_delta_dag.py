"""
Batch to Delta ingestion DAG template.

This DAG demonstrates how to perform a batch extraction of data and load it into a Delta Lake table.
It includes two placeholder tasks:
  1. extract_batch: to extract data from source systems such as S3, database, or API.
  2. transform_to_delta: to transform and load the extracted data into a Delta Lake table.

Replace the placeholder functions with your actual logic.
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def extract_batch(**context):
    """Placeholder to extract batch data from a source (e.g., S3, database, API)."""
    # TODO: implement extraction logic here
    print("Extracting batch data...")


def transform_to_delta(**context):
    """Placeholder to transform data and write it into a Delta Lake table."""
    # TODO: implement transformation and loading logic here
    print("Transforming and loading into Delta Lake...")

# Default arguments for the DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=10),
}

# Define the DAG for batch-to-Delta ingestion
with DAG(
    dag_id="batch_to_delta_template",
    description="Starter DAG for batch ingestion to Delta Lake",
    default_args=default_args,
    schedule_interval="@daily",  # Adjust schedule as needed
    catchup=False,
    tags=["batch", "delta", "template"],
) as dag:
    extract = PythonOperator(
        task_id="extract_batch",
        python_callable=extract_batch,
        provide_context=True,
    )

    transform = PythonOperator(
        task_id="transform_to_delta",
        python_callable=transform_to_delta,
        provide_context=True,
    )

    # Define task dependencies
    extract >> transform
