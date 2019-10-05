#!/usr/bin/env python
import socket
import sys
try:
    socket.inet_pton(socket.AF_INET6, sys.argv[1])
    result=0
except socket.error:
    result=1
sys.exit(result)
