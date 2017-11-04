#!/usr/bin/python

import sys

counter = dict()
max_count = 0
res_file = None


for line in sys.stdin:
    data = line.strip()
    counter[data] = counter.get(data, 0) + 1
    if counter[data] > max_count:
        max_count = counter[data]
        res_file = data

print res_file

    
