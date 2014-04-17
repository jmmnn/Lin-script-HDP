#!/usr/bin/env python
__author__ = 'jmmnn'

import subprocess
import sys

# Variables

#List commands to execute here.

#firewall and clock
NTPD = "sudo chkconfig ntpd on"
IPTABLES_OFF = "sudo chkconfig iptables off"
IPTABLES_STOP = "sudo /etc/init.d/iptables stop"
NTPD_START = "sudo service ntpd start"


#order commands in sequence
cmds = [NTPD, IPTABLES_OFF, IPTABLES_STOP, NTPD_START]

#Iterates over list, running statements for each item in the list
count=0
for cmd in cmds:
    count+=1
    print "Running Command Number %s" % count
    subprocess.call(cmd, shell=True)