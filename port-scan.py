#!/usr/bin/python

###
# Author: Ali Okan YUKSEL
# 2015-03-17
##
import socket, sys

try:
        host=sys.argv[1]
        port=sys.argv[2]
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        result = sock.connect_ex((host,int(port)))
        if result == 0:
                print "0"
                sys.exit(0)
        else:
                print "1"
                sys.exit(1)
except Exception as e:
        pass

print "1"
sys.exit(1)
