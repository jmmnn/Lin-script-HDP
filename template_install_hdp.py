#!/usr/bin/env python
__author__ = 'Jorge'

import subprocess

#List commands to execute here.
MESSAGES = "tail /var/log/messages"
SPACE = "df -h"
DIR = "ls -la"

#order them in sequence
cmds = [MESSAGES, SPACE, DIR]

#Iterates over list, running statements for each item in the list
#Note, that whitespace is absolutely critical and that a consistent indent must be maintained for the code to work properly
count=0
for cmd in cmds:
    count+=1
    print "Running Command Number %s" % count
    subprocess.call(cmd, shell=True)