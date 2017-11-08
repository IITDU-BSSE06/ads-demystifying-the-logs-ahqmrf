#!/usr/bin/python


import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, hyphen, hyphen2, time, gmt, request, path, req_type, status, code = data
        print "{0}".format(path)
