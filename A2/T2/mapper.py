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
    """product=p*q
    result=sum(x for x in product)"""
    result=product/(norm(p)*norm(q))
    return result

vFilename,peFilename=sys.argv[1:]
vfp=open(vFilename,"r")
rankDict=dict()
for line in vfp:
    node,rank=line.split(',')
    try:
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
        destinationList=json.loads(destinationList)#[x for x in destinationList[1:-1]]
        source=int(source)
    except:
        continue
    
    n=len(destinationList)

    for destination in destinationList:
        try:
            destination=int(destination)
            sourceEmbedding=pe[str(source)]#
            destEmbedding=pe[str(destination)]#
        except:
            continue
        if source in rankDict.keys():
            value=(rankDict[source]/n)*similarity(sourceEmbedding,destEmbedding)
        else:
            value=0
        print("{},{}".format(destination,value))