#!/usr/bin/env python
import sys

stateDict=dict()

for line in sys.stdin:
    line = line.strip()
    state,city,count = line.split("\t")
    state=state.strip()
    city=city.strip()

    try:
        count=int(count.strip())
    except ValueError:
        continue

    if state in stateDict.keys():
        if city in stateDict[state].keys():
            stateDict[state][city]+=count
        else:
            stateDict[state][city]=count
    else:
        stateDict[state]=dict()

for state,cityDict in stateDict.items():
    print(state)
    for city,count in cityDict.items():
        print(city,count)

