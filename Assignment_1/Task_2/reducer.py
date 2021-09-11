#! /usr/bin/env python3
import sys

previousState=""
previousCity=""
totalCount=0
totalStateCount=0

for line in sys.stdin:
    line = line.strip()
    state,city,count = line.split('\t')
    state=state.strip()
    city=city.strip()

    try:
        count=int(count.strip())
    except ValueError:
        continue
    
    if previousState!=state:
        if previousCity!='':
            print(previousCity,totalCount)
        if previousState!='':
            print(previousState,totalStateCount)
        print(state)
        previousState=state
        previousCity=city
        totalCount=count
        totalStateCount=count
    else:
        totalStateCount+=count
        if previousCity!=city:
            print(previousCity,totalCount)
            previousCity=city
            totalCount=count
        else:
            totalCount+=count
    
print(previousCity,totalCount)
print(previousState,totalStateCount)
