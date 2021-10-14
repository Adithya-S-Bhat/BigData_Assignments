#!/usr/bin/env python3

import sys

vertex=-1
sum=0

for line in sys.stdin:
    line=line.strip()
    node,contribution=line.split(',')
    try:
        node=int(node)
        contribution=float(contribution)
    except:
        continue

    if vertex!=-1:
        if vertex!=node:
            rank=0.15+(0.85*sum)
            print("{},{}".format(vertex,rank))
            vertex=node
            sum=contribution
        else:
            sum+=contribution
    else:
        vertex=node
        sum=contribution

rank=0.15+(0.85*sum)
print("{},{}".format(vertex,rank))
