Command to execute mapper.py locally:
cat ../US_ACCIDENT_DATA_5PERCENT.json | python3 mapper.py | sort -k1,1

Command to execute MR task locally:
cat ../US_ACCIDENT_DATA_5PERCENT.json | python3 mapper.py | sort -k1,1 | python3 reducer.py
