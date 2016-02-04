
def blosum(csv_file):
	lines = open(csv_file).readlines()
	aa = lines.pop(0).strip().split(',')
	mat = {}
	for line in lines:
		items = line.strip().split(',')
		a = items.pop(0)
		for i in range(len(items)):
			mat[(a,aa[i])] = int(items[i])
	return mat

blosum("blosum62.csv")