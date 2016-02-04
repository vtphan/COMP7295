'''
- blosum: read blosum files
- example: blosum("blosum60.txt")
'''

import re

def clean_line(line):
	return [ i for i in re.split('\s', line.strip()) if i!='' ]


def blosum(fn):
	lines = open(fn).readlines()
	lines = [ l for l in lines if not l.startswith('#')]
	
	if fn.endswith('.csv'):
		aa = lines.pop(0).strip().split(',')
	else:
		aa = clean_line(lines.pop(0))

	mat = {}
	for line in lines:
		if fn.endswith('.csv'):
			items = line.strip().split(',')
		else:
			items = clean_line(line)
		a = items.pop(0)
		for i in range(len(items)):
			mat[(a,aa[i])] = int(items[i])
	return mat

