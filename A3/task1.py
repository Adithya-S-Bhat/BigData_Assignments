from pyspark import SparkContext
from pyspark.sql.functions import *
from pyspark.sql import SQLContext
import sys

country,cityPath=sys.argv[1:]

spark_context = SparkContext.getOrCreate()
sqlContext=SQLContext(spark_context)

#option("header",True).
df=sqlContext.read.csv(cityPath,header = True,inferSchema=True)
noMissingdf=df.dropna(how='any',subset=['AverageTemperature'])

dfCountry=noMissingdf[noMissingdf.Country.isin(country)]
dfAvg=dfCountry.groupby("City").avg("AverageTemperature")
dfAvg=dfAvg.withColumnRenamed("avg(AverageTemperature)","avg")
dfAvg=dfAvg.withColumnRenamed("City","c")

dfJoin=dfCountry.join(dfAvg,noMissingdf.City==dfAvg.c,how="inner")
dfCityCount=dfJoin.filter(dfJoin["AverageTemperature"]>dfJoin["avg"]).groupby("City").count().orderBy("City")
cityCount=dfCityCount.collect()

for row in cityCount:
    print(row['City']+"\t"+str(row['count']))

"""rddCountry=dfCountry.rdd
rddCount=rddCountry.map()
rdd=spark_context.textFile(cityPath)
rdd.flatMap(lambda x:x.split(','))"""