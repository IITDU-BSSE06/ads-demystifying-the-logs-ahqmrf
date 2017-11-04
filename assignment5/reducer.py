#!/usr/bin/python

import sys

counter = set()

for line in sys.stdin:
    data = line.strip()
    counter.add(data)

print len(counter)

    
