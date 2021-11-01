from pyspark import SparkContext
from pyspark.sql.functions import *
from pyspark.sql import SQLContext
from pyspark.sql.types import *
import sys

cityPath,globalPath=sys.argv[1:]

spark_context = SparkContext.getOrCreate()
sqlContext=SQLContext(spark_context)

df=sqlContext.read.csv(cityPath,header = True,inferSchema=True)
df.AverageTemperature=df.AverageTemperature.cast(FloatType())
citydf=df.dropna(how='any',subset=['AverageTemperature','dt'])
#citydf.withColumn("AverageTemperature",df.AverageTemperature.cast('float'))
#citydf.AverageTemperature=citydf.AverageTemperature.cast(FloatType())

df=sqlContext.read.csv(globalPath,header = True,inferSchema=True)
df.LandAverageTemperature=df.LandAverageTemperature.cast(FloatType())
globaldf=df.dropna(how='any',subset=['LandAverageTemperature','dt'])
globaldf=globaldf.select("dt","LandAverageTemperature")
#globaldf.withColumn("LandAverageTemperature",df.LandAverageTemperature.cast('float'))
#globaldf.LandAverageTemperature=globaldf.LandAverageTemperature.cast(FloatType())

groupedDf=citydf.groupby("dt","Country").max("AverageTemperature")
groupedDf=groupedDf.withColumnRenamed("max(AverageTemperature)","max")

globaldf=globaldf.withColumnRenamed("dt","date")
globaldf.date=globaldf.date.cast(DateType())
groupedDf.dt=groupedDf.dt.cast(DateType())
joinDf=groupedDf.join(globaldf,globaldf.date==groupedDf.dt,how="inner")

joinDf.LandAverageTemperature=joinDf.LandAverageTemperature.cast(FloatType())
joinDf.max=joinDf.max.cast(FloatType())
resultDf=joinDf.filter(joinDf['max'] > joinDf['LandAverageTemperature']).groupBy("Country").count().orderBy("Country")

result=resultDf.collect()

for row in result:
    print(row["Country"]+"\t"+str(row["count"]))