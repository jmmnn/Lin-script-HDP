#!/usr/bin/env python
__author__ = 'Jorge'

import subprocess
import sys

# Variables
Key = "us-east.pem"
User = str(sys.argv[1])
PublicDNS = str(sys.argv[2])
print "Public DNS", PublicDNS
print "Key", Key

#List commands to execute here.
NTPD = "sudo chkconfig ntpd on"
IPTABLES-OFF = "sudo chkconfig iptables off"
IPTABLES-STOP = "sudo /etc/init.d/iptables stop"
NTPD-START = "sudo service ntpd start"

#order them in sequence
cmds = [NTPD, IPTABLES-OFF, IPTABLES-STOP, NTPD-START]

#Iterates over list, running statements for each item in the list
#Note, that whitespace is absolutely critical and that a consistent indent must be maintained for the code to work properly
count=0
for cmd in cmds:
    count+=1
    print "Running Command Number %s" % count
    subprocess.call(cmd, shell=True)