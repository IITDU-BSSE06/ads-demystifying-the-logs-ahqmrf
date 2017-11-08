#!/usr/bin/python

import sys

counter = dict()


for line in sys.stdin:
    data = line.strip().split('"')[1]
    counter[data] = counter.get(data, 0) + 1

for key in counter:
    print "{0} {1}".format(key, counter[key])

    
