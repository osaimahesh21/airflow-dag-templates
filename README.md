# airflow-dag-templates

Collection of Airflow DAG templates for CDC, batch-to-Delta, and streaming ingestion.

## Overview

This repository contains starter DAGs that you can use as templates for common ingestion patterns in Apache Airflow. Each DAG is fully commented and includes placeholder functions where you can implement your own extraction, transformation and loading logic.

### Included templates

- **cdc_dag.py** – A Change Data Capture (CDC) template that illustrates how to capture incremental changes from a source system and load them into a target. It defines a DAG with a single `capture_changes` task and can be scheduled hourly by default.
- **batch_to_delta_dag.py** – A batch ingestion template that extracts data from a batch source and writes it into a Delta Lake table. It contains two tasks, `extract_batch` and `transform_to_delta`, scheduled daily.
- **streaming_ingestion_dag.py** – A streaming ingestion template that reads events from a streaming source (like Kafka, Kinesis, or Pub/Sub) and processes each event or micro‑batch. This DAG has tasks `read_stream` and `process_event`, and it has no schedule interval because streaming jobs often run continuously.

## Usage

1. **Clone this repository** and copy the desired DAG file(s) into your Airflow `dags/` directory.
2. **Install any dependencies** required by your implementation (e.g., connectors for your source systems and Delta Lake).
3. **Customize the placeholder functions**:
    - Replace the bodies of functions such as `capture_changes`, `extract_batch`, `transform_to_delta`, `read_stream`, and `process_event` with your own logic to read, process, and write data.
    - Adjust any configuration constants (e.g., table names, connection identifiers) as needed.
4. **Adjust scheduling**:
    - The CDC template is scheduled hourly by default via `schedule_interval="@hourly"`. Modify this string or use a `timedelta` object to change the frequency.
    - The batch-to-Delta template uses a daily schedule (`"@daily"`). Change `schedule_interval` if you need a different cadence.
    - The streaming template uses `schedule_interval=None` because streaming jobs usually run continuously; if you need a periodic trigger, set an appropriate schedule.
5. **Deploy and monitor** the DAGs using the Airflow UI. Ensure that your Airflow environment has access to the resources necessary for extraction and loading.

These templates are meant to provide a clean starting point so you can focus on implementing the specific business logic of your data pipelines.
