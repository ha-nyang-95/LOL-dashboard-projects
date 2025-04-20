FROM apache/airflow:2.8-python3.10
USER root

# 시스템 도구
RUN apt-get update && apt-get install -y gcc

# 파이썬 패키지
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

USER airflow
