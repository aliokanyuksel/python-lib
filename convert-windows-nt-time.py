#!/usr/bin/env python

##
# author: Ali Okan Yuksel
# e-mail: aliokan.yuksel[at]siyahsapka.org
##
import datetime
import sys


def windowstime2datetime(nttime):
	nttime=long(nttime)
	seconds = nttime / 10000000
	epoch = seconds - 11644473600
	dt = datetime.datetime(2000, 1, 1, 0, 0, 0)
	dt=dt.fromtimestamp(epoch)
	return dt

def getdiffnttime(nttime):
	if nttime.strip()=="":
		return
	try:
		dt=windowstime2datetime(nttime)
		now=datetime.datetime.now()
		return (now-dt).total_seconds()/86400
	except:
		pass
	return

print int(round(getdiffnttime(sys.argv[1])))
