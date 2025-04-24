import os, json
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import MapType, StringType

KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "kafka:9092")
PG_URL = os.getenv("PG_JDBC")
PG_USER = os.getenv("PG_USER")
PG_PW = os.getenv("PG_PW")

spark = (SparkSession.builder
         .appName("KafkaToPostgres")
         .getOrCreate())

# 예: 모든 topic(*_csv) 수신
df = (spark.readStream
      .format("kafka")
      .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP)
      .option("subscribePattern", ".*csv")
      .option("startingOffsets", "latest")
      .load())

json_df = df.selectExpr("CAST(topic AS STRING)", "CAST(value AS STRING) as json_str")

def foreach_batch_func(batch_df, epoch_id):
    for topic in set(row.topic for row in batch_df.select('topic').distinct().collect()):
        subset = batch_df.filter(col("topic") == topic).select("json_str")
        table = topic   # topic명이 그대로 테이블
        schema_df = subset.select(from_json("json_str", MapType(StringType(), StringType())).alias("data"))
        flat_df = schema_df.selectExpr("data.*")
        (flat_df.write
               .mode("append")
               .format("jdbc")
               .option("url", PG_URL)
               .option("dbtable", table)
               .option("user", PG_USER)
               .option("password", PG_PW)
               .save())

(json_df.writeStream
        .foreachBatch(foreach_batch_func)
        .outputMode("append")
        .start()
        .awaitTermination())
