#!/usr/bin/env python
import sys
import json
import math
import requests

def isNotNan(data):
    if type(data["Description"])!=str:
        if math.isnan(data["Description"]):
            return False
    if type(data["Sunrise_Sunset"])!=str:
        if math.isnan(data["Sunrise_Sunset"]):
            return False
    if type(data["Weather_Condition"])!=str:
        if math.isnan(data["Weather_Condition"]):
            return False
    if math.isnan(data["Severity"]) or math.isnan(data["Visibility(mi)"]) or math.isnan(data["Precipitation(in)"]):
        return False
    return True

centreLat,centreLong,D = sys.argv[1:]
centreLat=float(centreLat)
centreLong=float(centreLong)
D=float(D)

for line in sys.stdin:
    line=line.strip()
    data = json.loads(line)

    if(isNotNan(data)):
        lat=data["Start_Lat"]
        long=data["Start_Lng"]
        euclidDist=math.sqrt(((long-centreLong)**2) + ((lat-centreLat)**2))
        if(euclidDist<=D):
            p={"latitude":lat,"longitude":long}
            response=requests.post("http://35.231.8.198:5000",json=p).json()
            city=response["city"]
            state=response["state"]
            print(state+"\t"+city+"\t1")
