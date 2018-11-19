import random
import math
from collections import defaultdict
from nltk.stem import WordNetLemmatizer
from lib import trimAbstract

class InformationContent:
	icVal = dict()

	def __init__(self, FILENAME):
		f = open(FILENAME, "r")
		vals = f.readline().split()
		self.minVal, self.maxVal = float(vals[0]), float(vals[1])


		while True:
			line = f.readline()
			if not line: break
			key, value = line.split()
			self.icVal[key] = float(value)


	def getInformationContent(self, word):	
		if word not in self.icVal:
			return self.maxVal		
		return self.icVal[word]

	# def printSortedValues(self):
	# 	newSort = sorted(self.sorting, key=lambda x: x[0])
	# 	for val in newSort:
	# 		print(val)
