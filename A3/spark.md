cd
sudo rm spark-*
sudo rm -rf spark-*


# Installing Scala and Git
sudo apt install scala git -y


# Downloading and setting up Spark
wget https://downloads.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
tar xzf spark-3.1.2-bin-hadoop3.2.tgz
sudo mv spark-3.1.2-bin-hadoop3.2 /opt/spark


# Configuring Spark
sudo echo "export SPARK_HOME=/opt/spark" >> ~/.profile
sudo echo "export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin" >> ~/.profile
sudo echo "export PYSPARK_PYTHON=/usr/bin/python3" >> ~/.profile


# Starting Spark
cd /opt/spark/sbin
sudo chmod +x *.sh

cd /opt/spark/bin
sudo chmod +x pyspark 
sudo chmod +x spark-shell
sudo chmod +x spark-submit

./spark-shell


cd
/opt/spark/bin/pyspark --version
/opt/spark/bin/pyspark
to exit:ctrl+d
To check if spark is running: /opt/spark/bin/spark-submit --version

wget -c https://drive.google.com/uc?id=1d0bVb8T9osaL0_jB0Q8rj3C_t6nMIS-X -O inp1.txt
cat inp1.txt
/opt/spark/bin/pyspark

WordCount Program:
from pyspark import SparkContext
import sys
text_file = sc.textFile("./inp1.txt")#inp.txt would be in hdfs
#sc=SparkContext('local',"task1")
print(text_file.take(100))#to get contents of file-transformation
print(text_file)#this just tells its a mappartition rdd
rdd1_flatmap=text_file.flatMap(lambda line:line.split(" "))
print(rdd1_flatmap.take(100))
rdd2_map=rdd1_flatmap.map(lambda word:(word,1))
print(rdd2_map.take(100))
counts=rdd2_map.reduceByKey(lambda a,b:a+b)#action!!
print(counts.take(100))
counts.saveAsTextFile("./op1")

Load .py file to spark:
/opt/spark/bin/spark-submit wordcount.py
or
/opt/spark/bin/pyspark < wordcount.py
#rm -rf op1/

Dataframes:
wget -c https://drive.google.com/uc?id=1Tcx9wOJrytuemmECF8gtYAeighU8OcRJ -O inp2.json
/opt/spark/bin/pyspark
df1=sqlContext.read.text("./inp1.txt")
df=sqlContext.read.json("./inp2.json")
df.show(5)
df.select("author","title","rank"),show()

Author is "Stephenie Meyer":
df[df.author.isin("John Sandford","Stephenie Meyer")].show(5)
#isn is "in" in sql 

df.select("author","title",df.title.like("%THE%)).show(5)
Delete column:
df_del=df.drop("amazon_product_url")
df_del.show(5)

df_grp=df.groupBy("author").count().orderBy("count",ascending=0).show(10)
df to RDD:
rdd1=df.rdd
rdd1.take(5)
RDD to df:
df2=rdd1.toDF()
df2.show()

/opt/spark/bin/pyspark
rdd1=sc.parallelize([1,2,3,4,5,10])
rdd2=sc.parallelize([2,3,7,8,10])
print(rdd1.intersection(rdd2).collect())
print(rdd1.cartesian(rdd2).collect())
rdd3=sc.parallelize([("abc",[1,3]),("xyz",2)])
rdd4=something similar to rdd3
rdd5=rdd3.join(rdd4)
rdd5.take(10)

rdd1=spark.sparkContext.parallelize(["abc",1)...
rdd2=
df1=spark.createDataFrame(rdd1,schema=['k','v1'])
df2=spark.createDataFrame(rdd2,schema=['k','v2'])
df3=df1.join(df2,df1.k==df2.k,how="inner")
df3.show()


df=sqlContext.read.csv("BigData_Assignments/A3/city_sample_5percent.csv",header = True,inferSchema=True)
citydf=df.dropna(how='any',subset=['AverageTemperature'])
df=sqlContext.read.csv("BigData_Assignments/A3/global.csv",header = True,inferSchema=True)
globaldf=df.dropna(how='any',subset=['LandAverageTemperature'])



$SPARK_HOME/bin/spark-submit task1.py India city_sample.csv > output_sample_t1.txt 2> log_t1.txt
$SPARK_HOME/bin/spark-submit task2.py city_sample.csv global_sample.csv 2> log.txt > output_sample_t2.txt
