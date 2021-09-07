#!/usr/bin/env python
import sys
import json
from datetime import datetime

for line in sys.stdin:
    line=line.strip()
    data = json.loads(line)
    #filter(word)

    #2017-02-07 13:32:33.354
    try:
        dateTimeObject=datetime.strptime(str(data["Start_Time"]).strip(),"%Y-%m-%d %H:%M:%S.%f")
    except ValueError:
        print(data["Start_Time"])
        dateTimeObject=datetime.strptime(str(data["Start_Time"]).strip(),"%Y-%m-%d %H:%M:%S")
    
    hour=datetime.strftime(dateTimeObject,"%H")
    print(hour,"\t1")