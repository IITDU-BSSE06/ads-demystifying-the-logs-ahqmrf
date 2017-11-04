#!/usr/bin/python

import sys

count = 0
path = "/assets/js/the-associates.js"

for line in sys.stdin:
    if path == line.strip():
        count = count + 1
	
print count
