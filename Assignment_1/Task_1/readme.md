Command to execute mapper.py locally:
cat ../US_ACCIDENT_DATA_5PERCENT.json | python3 mapper.py | sort -k1,1

Command to execute MR task locally:
cat ../US_ACCIDENT_DATA_5PERCENT.json | python3 mapper.py | sort -k1,1 | python3 reducer.py

Steps to execute on HadoopDistributedFileSystem(hdfs):
1. Create input directory(A1/input):  
	hdfs dfs -mkdir /A1
	hdfs dfs -mkdir /A1/input/
2. Load the file into hdfs directory using command:  
	hdfs dfs -put ~/BigData_Assignments/Assignment_1/US_ACCIDENT_DATA_5PERCENT.json /A1/input
3. Check the contents of input directory using command:  
	hdfs dfs -ls /A1/input
4. Convert mapper.py and reducer.py to executable files:
	chmod +x ~/BigData_Assignments/Assignment_1/Task_1/mapper.py ~/BigData_Assignments/Assignment_1/Task_1/reducer.py
5. Run MapReduce(MR) job:  
	hadoop jar /home/pes1ug19cs027/hadoop-3.2.2/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar -input /A1/input/US_ACCIDENT_DATA_5PERCENT.json -output /A1/output_T1 -mapper "/home/pes1ug19cs027/BigData_Assignments/Assignment_1/Task_1/mapper.py" -reducer "/home/pes1ug19cs027/BigData_Assignments/Assignment_1/Task_1/reducer.py"
6. Go to hdfs file explorer in browser:
	http://localhost:9870/explorer.html#/A1/output_T1
7. Download part-00000
