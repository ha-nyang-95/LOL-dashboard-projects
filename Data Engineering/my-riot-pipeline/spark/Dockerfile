FROM bitnami/spark:3.5

# Kafka 커넥터 JAR 추가
ADD https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.5.1/spark-sql-kafka-0-10_2.12-3.5.1.jar /opt/bitnami/spark/jars/
ADD https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.6.0/kafka-clients-3.6.0.jar /opt/bitnami/spark/jars/

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt