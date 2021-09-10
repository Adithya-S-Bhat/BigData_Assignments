#!/usr/bin/env python
import sys
import json
import math
import requests

def isNotNan(data):
    if math.isnan(data["Start_Lat"]) or math.isnan(data["Start_Lng"]):
        return False
    return True

centreLat,centreLong,D = sys.argv[1:]
centreLat=float(centreLat.strip())
centreLong=float(centreLong.strip())
D=float(D)

for line in sys.stdin:
    line=line.strip()
    data = json.loads(line)

    if(isNotNan(data)):
        lat=data["Start_Lat"]
        long=data["Start_Lng"]
        #euclidDist=math.sqrt(((long-centreLong)**2) + ((lat-centreLat)**2))
        euclidDist=math.dist([lat,long],[centreLat,centreLong])
        if(euclidDist<=D):
            p={"latitude":lat,"longitude":long}
            response=requests.post("http://20.185.44.219:5000/",json=p).json()
            city=response["city"].strip()
            state=response["state"].strip()
            print("{}\t{}\t1".format(state,city))
