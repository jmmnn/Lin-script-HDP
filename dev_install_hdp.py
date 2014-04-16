#!/usr/bin/env python
__author__ = 'Jorge'

import subprocess
import sys

# Variables

#List commands to execute here.

#firewall and clock
NTPD = "sudo chkconfig ntpd on"
IPTABLES_OFF = "sudo chkconfig iptables off"
IPTABLES_STOP = "sudo /etc/init.d/iptables stop"
NTPD_START = "sudo service ntpd start"

#install ambari
CD = "cd /etc/yum.repos.d/"
GET_AMBARI_REPO = "wget http://public-repo-1.hortonworks.com/ambari/centos6/1.x/updates/1.5.0/ambari.repo"
UPDATE_REPOS = "sudo yum repolist"
INSTALL_AMBARI = "sudo yum install ambari-server"
SETUP_AMBARI = "ambari-server setup"
START_AMBARI = "ambari-server start"



#order them in sequence
cmds = [NTPD, IPTABLES_OFF, IPTABLES_STOP, NTPD_START, CD, GET_AMBARI_REPO, UPDATE_REPOS, INSTALL_AMBARI, SETUP_AMBARI, START_AMBARI]

#Iterates over list, running statements for each item in the list
#Note, that whitespace is absolutely critical and that a consistent indent must be maintained for the code to work properly
count=0
for cmd in cmds:
    count+=1
    print "Running Command Number %s" % count
    subprocess.call(cmd, shell=True)