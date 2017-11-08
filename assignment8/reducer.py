#!/usr/bin/python

import sys

from urlparse import urlparse

counter = dict()
max_count = 0
res_file = None


for line in sys.stdin:
    data = line.strip()
    res = urlparse(data)
    temp = data.split("/")
    if res.geturl() != "http://www.the-associates.co.uk":
	    counter[res.path] = counter.get(res.path, 0) + 1
	    if counter[res.path] > max_count:
		max_count = counter[res.path]
		res_file = res.path

print "{0} {1}".format(res_file, max_count)

