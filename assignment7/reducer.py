#!/usr/bin/python

import sys

counter = 0


for line in sys.stdin:
    data = line.strip().split('"')
    get = data[1]
    if get == "GET" :
        counter = counter + 1


print "GET {0}".format(counter)

    
