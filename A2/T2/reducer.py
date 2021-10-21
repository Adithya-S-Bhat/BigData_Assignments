#!/usr/bin/env python3

import sys
import math

vertex=-1
sum=0
isSource=0

for line in sys.stdin:
    line=line.strip()
    node,contribution=line.split(' ')
    try:
        node=int(node)
        contribution=float(contribution)
    except:
        continue

    """if vertex!=-1:
        if vertex!=node:
            if isSource==1:
                rank=0.15+(0.85*sum)
                print("{}, {:.2f}".format(vertex,rank))
            if contribution=='$':
                isSource=1
                vertex=node
                sum=0
            else:
                isSource=0
        else:
            if isSource==1:
                try:
                    contribution=float(contribution)
                except:
                    continue
                sum+=contribution
    else:
        if contribution=='$':
            isSource=1
            vertex=node
            sum=0"""

    if vertex!=-1:
        if vertex!=node:
            rank=0.15+(0.85*sum)
            print("{},{:.2f}".format(vertex,rank))
            vertex=node
            sum=contribution
        else:
            sum+=contribution
    else:
        vertex=node
        sum=contribution

#if vertex!=-1 and isSource==1:
if vertex!=-1:
    rank=round(0.15+(0.85*sum),2)
    print("{},{:.2f}".format(vertex,rank))
