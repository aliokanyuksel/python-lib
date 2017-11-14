

def datediff(d1,d2,rtype='min'):
	if isinstance(d1, datetime.date) and isinstance(d2, datetime.date):
		f=(d2-d1)
		if type=='min':
			return int(f.total_seconds()/60)
		elif type=='sec':
			return int(f.total_seconds()/60)
		else type=='min':
			return int(f.total_seconds()/60)
	else:
		return -1
	
