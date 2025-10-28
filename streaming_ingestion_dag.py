"""
Streaming ingestion DAG template.

This DAG demonstrates how to ingest data from a streaming source and load it into downstream systems.
It includes two placeholder tasks:
  1. read_stream: to continuously read from a streaming source like Kafka, Kinesis, or Pub/Sub.
  2. process_event: to process each event or micro-batch from the stream.

Replace the placeholder functions with your actual streaming logic.
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def read_stream(**context):
    """Placeholder to read data from a streaming source (e.g., Kafka, Kinesis, Pub/Sub)."""
    # TODO: implement streaming read logic here
    print("Reading from streaming source...")


def process_event(**context):
    """Placeholder to process an event or micro-batch and write to a target system."""
    # TODO: implement event processing logic here
    print("Processing event/micro-batch...")

# Default arguments for the DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 1, 1),
    "retries": 0,
}

# Define the DAG for streaming ingestion
with DAG(
    dag_id="streaming_ingestion_template",
    description="Starter DAG for streaming ingestion",
    default_args=default_args,
    schedule_interval=None,  # Streaming jobs typically run continuously
    catchup=False,
    tags=["streaming", "template"],
) as dag:
    read = PythonOperator(
        task_id="read_stream",
        python_callable=read_stream,
        provide_context=True,
    )

    process = PythonOperator(
        task_id="process_event",
        python_callable=process_event,
        provide_context=True,
    )

    # Define task dependencies
    read >> process
