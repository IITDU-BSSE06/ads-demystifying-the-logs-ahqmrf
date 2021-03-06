#!/usr/bin/python

import sys

counter = dict()


for line in sys.stdin:
    data = line.strip().split("/")
    date = data[0]
    month = data[1]
    year = data[2].split(":")[0]
    counter[year] = counter.get(year, 0) + 1


print "2009 {0}".format(counter["2009"])
print "2010 {0}".format(counter["2010"])
print "2011 {0}".format(counter["2011"])

res = "2009"
max_count = counter["2009"]
if max_count < counter["2010"]:
    res = "2010"
    max_count = counter["2010"]
if max_count < counter["2011"]:
    res = "2011"
    max_count = counter["2011"]

print "Year {0} had most number of hits".format(res)

    
