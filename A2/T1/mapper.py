#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line=line.strip()
    source,destination=line.split()
    print("{} {}".format(source,destination))