#!/usr/bin/env python
import sys

countDict=dict()

for line in sys.stdin:
    line = line.strip()
    hour, count = line.split("\t")

    try:
        count=int(count)
        hour=int(hour)
    except ValueError:
        continue

    if hour in countDict.keys():
        countDict[hour]+=count
    else:
        countDict[hour]=count

for hour,count in countDict.items():
    print(hour,count)