from pyspark import SparkContext
from pyspark.sql.functions import *
from pyspark.sql import SQLContext
from pyspark.sql.types import *
import sys

cityPath,globalPath=sys.argv[1:]

spark_context = SparkContext.getOrCreate()
sqlContext=SQLContext(spark_context)

df=sqlContext.read.csv(cityPath,header = True,inferSchema=True)
citydf=df.dropna(how='any',subset=['AverageTemperature'])
#citydf.withColumn("AverageTemperature",df.AverageTemperature.cast('float'))
citydf.AverageTemperature=citydf.AverageTemperature.cast(FloatType())

df=sqlContext.read.csv(globalPath,header = True,inferSchema=True)
globaldf=df.dropna(how='any',subset=['LandAverageTemperature'])
globaldf=globaldf.select("dt","LandAverageTemperature")
#globaldf.withColumn("LandAverageTemperature",df.LandAverageTemperature.cast('float'))
globaldf.AverageTemperature=globaldf.LandAverageTemperature.cast(FloatType())

groupedDf=citydf.groupby("dt","Country").max("AverageTemperature")
groupedDf=groupedDf.withColumnRenamed("max(AverageTemperature)","max")

globaldf=globaldf.withColumnRenamed("dt","date")
joinDf=groupedDf.join(globaldf,globaldf.date==groupedDf.dt,how="inner")

resultDf=joinDf.filter(joinDf['max']>joinDf['LandAverageTemperature']).groupBy("Country").count().orderBy("Country")

result=resultDf.collect()

for row in result:
    print(row["Country"]+"\t"+str(row["count"]))