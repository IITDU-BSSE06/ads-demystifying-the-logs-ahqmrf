#!/usr/bin/python


import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, hyphen, hyphen, time, gmt, request, path, req_type, status, code = data
        print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}".format(ip, time.split("[")[1], gmt.split("]")[0].split("-")[0], request.split("\"")[1], path.split("\"")[0], status, code)
