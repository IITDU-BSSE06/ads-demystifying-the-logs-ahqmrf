#!/usr/bin/python

import sys

count = 0
ip = "10.99.99.186"

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) == 7:
        if ip == data_mapped[0].strip():
            count = count + 1
	
print count
