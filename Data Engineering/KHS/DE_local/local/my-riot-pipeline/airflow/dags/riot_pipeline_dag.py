from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import os
import subprocess

SCRIPTS_DIR = "/opt/airflow/scripts"
KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "kafka:9092")

def run_extract():
    subprocess.check_call(["python", f"{SCRIPTS_DIR}/extract_timeline_matches_json.py"])

def run_split_push():
    # 1) split_matches_data.py → CSV
    subprocess.check_call(["python", f"{SCRIPTS_DIR}/split_matches_data.py"])
    # 2) 각 CSV를 Kafka로 전송 (간단 예시)
    import glob, kafka, csv
    producer = kafka.KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP,
                                   value_serializer=lambda v: v.encode())
    for csv_path in glob.glob(f"{SCRIPTS_DIR}/specific_data/**/*.csv", recursive=True):
        topic = Path(csv_path).stem.replace('.', '_')
        with open(csv_path, newline='') as f:
            for row in csv.DictReader(f):
                producer.send(topic, json.dumps(row))
    producer.flush()

with DAG(
    dag_id="riot_match_timeline_pipeline",
    schedule_interval="*/10 * * * *",  # 매 시 0분
    start_date=days_ago(1),
    catchup=False,
) as dag:

    extract_json = PythonOperator(
        task_id="extract_timeline_matches_json",
        python_callable=run_extract,
    )

    split_and_produce = PythonOperator(
        task_id="split_matches_data_and_push_kafka",
        python_callable=run_split_push,
    )

    extract_json >> split_and_produce
