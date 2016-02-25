Distance = {}
Label = []

class Node(object):
	def __init__(self, label, left=None, right=None):
		self.label = label
		self.left = left
		self.right = right

	def print(self):
		if self.left is None and self.right is None:
			print(self.label, end="")
		else:
			print("(", end="")
			self.left.print()
			print(",", end="")
			self.right.print()
			print(")", end="")

def Initialize(distance_file):
	with open(distance_file) as f:
		for line in f:
			items = line.strip().split(" ")
			Label.append(items[0])
			for i, lab in enumerate(Label):
				if i<len(Label)-1:
					Distance[lab,items[0]] = Distance[items[0],lab] = float(items[i+1])

