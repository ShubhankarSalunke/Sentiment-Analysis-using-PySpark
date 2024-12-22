# Required imports
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
from textblob import TextBlob

spark = SparkSession.builder \
    .appName("SentimentAnalysis") \
    .getOrCreate()

data = spark.read.csv("dataset.csv", header=True, inferSchema=True)

data = data.na.drop(subset=["text_column"]) 
data = data.withColumnRenamed("text_column", "text")

def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"

sentiment_udf = udf(get_sentiment, StringType())

data = data.withColumn("sentiment", sentiment_udf("text"))

data.select("text", "sentiment").show(10)

data.write.csv("sentiment_results.csv", header=True)

spark.stop()
