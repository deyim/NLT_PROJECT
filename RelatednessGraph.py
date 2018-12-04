from collections import defaultdict
from graph_tool.all import *
class RelatednessGraph:

	def __init__(self, input_file):
		self.input_file = input_file
		self.rel_graph = self.readRelFile(self.input_file)


	def readRelFile(self, input_file):
		f = open(input_file, "r")

		graph_ds = defaultdict(list)
		while True:
			line = f.readline()
			if not line: break
			from_node, to_node, rel = line.split('\t')
			if float(rel) < 3.5: 
				rel = 0
			ary[from_node].append((to_node, rel))

		return graph_ds

	def sortForOnePaper(self):		
		for key, val in self.rel_graph.items():
			print(key)
			for i in range(:10):
				print(val[i][1])
			for j in range(10:):
				print(val[i][1])

	def drawGraph(self):
		g = Graph(directed=False)




