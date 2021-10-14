#!/bin/sh
CONVERGE=1
ITER=1
rm v v1 log*

cat dataset_1percent.txt\
| python3 "/home/pes1ug19cs027/BigData_Assignments/A2/T1/mapper.py" \
| sort -k 1,1\
| python3 /home/pes1ug19cs027/BigData_Assignments/A2/T1/reducer.py /home/pes1ug19cs027/BigData_Assignments/A2/v \
>adjList.txt

while [ "$CONVERGE" -ne 0 ]
do
	echo "############################# ITERATION $ITER #############################"
	
	cat adjList.txt\
	| python3 /home/pes1ug19cs027/BigData_Assignments/A2/T2/mapper.py /home/pes1ug19cs027/BigData_Assignments/A2/v /home/pes1ug19cs027/BigData_Assignments/A2/embedding_1percent.json\
	| sort -k 1,1\
	| python3 /home/pes1ug19cs027/BigData_Assignments/A2/T2/reducer.py\
	>v1
	
	CONVERGE=$(python3 check_conv.py $ITER>&1)
	ITER=$((ITER+1))
	
	echo $CONVERGE
done
