def Initialize(distance_file, distance, label):
	with open(distance_file) as f:
		for line in f:
			items = line.strip().split(" ")
			label.append(items[0])
			for i, lab in enumerate(label):
				if i<len(Label)-1:
					distance[lab,items[0]] = distance[items[0],lab] = float(items[i+1])

class Node(object):
	def __init__(self, label, left=None, right=None):
		self.label = label
		self.left = left
		self.right = right

	def Newick(self):
		if self.left is None and self.right is None:
			print(self.label, end="")
		else:
			print("(", end="")
			self.left.Newick()
			print(",", end="")
			self.right.Newick()
			print(")", end="")


A = Node('A'); B = Node('B'); C = Node('c', A, B); D = Node('D'); root = Node('e', D, C)
root.Newick()

Distance = {}
Label = []
Initialize("phylo_distance.txt", Distance, Label)
print( Distance['A','B'], Distance['B','A'])

