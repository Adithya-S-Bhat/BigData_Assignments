from pyspark import SparkContext
from pyspark.sql.functions import *
from pyspark.sql import SQLContext
import sys

cityPath,globalPath=sys.argv[1:]

spark_context = SparkContext.getOrCreate()
sqlContext=SQLContext(spark_context)

df=sqlContext.read.csv(cityPath,header = True,inferSchema=True)
citydf=df.dropna(how='any',subset=['AverageTemperature'])

df=sqlContext.read.csv(globalPath,header = True,inferSchema=True)
globaldf=df.dropna(how='any',subset=['LandAverageTemperature'])

groupedDf=df.groupby("dt","Country").max("AverageTemperature")