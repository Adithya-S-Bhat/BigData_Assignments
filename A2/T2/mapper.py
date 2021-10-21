#!/usr/bin/env python3

import sys
import json

def norm(p):
    sum=0
    for i in p:
        try:
            i=float(i)
        except:
            continue
        sum+=(i*i)
    return (sum**0.5)

def similarity(p,q):
    product=0
    for i in range(len(p)):
        try:
            element1=float(p[i])
            element2=float(q[i])
            product+=element1*element2
        except:
            continue
    result=product/(norm(p)*norm(q))
    return result

vFilename,peFilename=sys.argv[1:]
vfp=open(vFilename,"r")
rankDict=dict()
for line in vfp:
    line=line.strip()
    node,rank=line.split(',')
    try:
        rank=rank.strip()
        rank=float(rank)
        node=int(node)
    except:
        continue
    rankDict[node]=rank

pefp=open(peFilename,"r")
pe=json.load(pefp)

for line in sys.stdin:
    line=line.strip()
    source,destinationList=line.split('$')

    try:
        destinationList=json.loads(destinationList)
        source=int(source)
    except:
        continue
    
    n=len(destinationList)
    contribution=rankDict[source]/n
    print("{} 0".format(source))

    for destination in destinationList:
        try:
            destination=int(destination)
            sourceEmbedding=pe[str(source)]
            destEmbedding=pe[str(destination)]
        except:
            continue
        value=contribution*similarity(sourceEmbedding,destEmbedding)
        print("{} {}".format(destination,value))