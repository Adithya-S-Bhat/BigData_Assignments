#!/usr/bin/env python3

import sys

destinationNodes=[]
sourceNode=" "
filename=sys.argv[1]
fp=open(filename,"w")


for line in sys.stdin:
    line=line.strip()
    source,destination=line.split('\t')
    try:
        destination=int(destination)
    except:
        continue

    if sourceNode!=" ":
        if source==sourceNode:
            destinationNodes.append(destination)
        else:
            print("{}${}".format(sourceNode,destinationNodes))
            fp.write("{},1\n".format(sourceNode))
            destinationNodes.clear()
            destinationNodes.append(destination)
            sourceNode=source
    else:
        sourceNode=source
        destinationNodes.append(destination)


print("{}${}".format(source,destinationNodes))
fp.write("{},1".format(sourceNode))
fp.close()