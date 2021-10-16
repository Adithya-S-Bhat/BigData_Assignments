#!/usr/bin/env python3

import sys

destinationNodes=[]
sourceNode=-1
filename=sys.argv[1]
fp=open(filename,"w")

for line in sys.stdin:
    line=line.strip()
    source,destination=line.split(' ')
    try:
        source=int(source)
        destination=int(destination)
    except:
        continue

    if sourceNode!=-1:
        if source==sourceNode:
            destinationNodes.append(destination)
        else:
            print("{}${}".format(sourceNode,destinationNodes))
            destinationNodes.clear()
            destinationNodes.append(destination)
            sourceNode=source
            fp.write("{}, 1\n".format(sourceNode))
    else:
        sourceNode=source
        destinationNodes.append(destination)
        fp.write("{}, 1\n".format(sourceNode))

if sourceNode!=-1:
    print("{}${}".format(source,destinationNodes))
fp.close()