FROM apache/airflow:2.8.3-python3.10
USER root

# 시스템 도구
RUN apt-get update && apt-get install -y gcc

USER airflow
# 파이썬 패키지
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt