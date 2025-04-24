from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from pathlib import Path
import os
import subprocess
import glob
import json
import csv
from kafka import KafkaProducer

SCRIPTS_DIR = "/opt/airflow/scripts"
KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "kafka:9092")

def run_extract():
    try:
        print("=== RUNNING extract_timeline_matches_json ===")
        subprocess.check_call(["python", f"{SCRIPTS_DIR}/extract_timeline_matches_json.py"])
        print("=== DONE extract_timeline_matches_json ===")
    except subprocess.CalledProcessError as e:
        print(f"extract 실패: {e}")
        raise

def run_split_push():
    try:
        print("=== RUNNING split_matches_data ===")
        subprocess.check_call(["python", f"{SCRIPTS_DIR}/split_matches_data.py"])

        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP,
            value_serializer=lambda v: v.encode()
        )
        for csv_path in glob.glob(f"{SCRIPTS_DIR}/specific_data/**/*.csv", recursive=True):
            topic = Path(csv_path).stem.replace('.', '_')
            with open(csv_path, newline='') as f:
                for row in csv.DictReader(f):
                    producer.send(topic, json.dumps(row))
        producer.flush()
        print("=== DONE split_matches_data ===")
    except Exception as e:
        print(f"split 실패: {e}")
        raise

with DAG(
    dag_id="riot_pipeline_dag",
    schedule_interval="*/30 * * * *",
    start_date=days_ago(1),
    catchup=False,
) as dag:

    extract_json = PythonOperator(
        task_id="extract_timeline_matches_json",
        python_callable=run_extract,
    )

    split_and_produce = PythonOperator(
        task_id="split_matches_data",
        python_callable=run_split_push,
    )

    extract_json >> split_and_produce
