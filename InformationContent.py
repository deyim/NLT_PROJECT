import random
import math
import operator
from collections import defaultdict
from nltk.stem import WordNetLemmatizer
from lib import trimAbstract

class InformationContent:
	icVal = dict()

	def __init__(self, FILENAME):
		f = open(FILENAME, "r")
		self.minVal, self.maxVal = map(float, f.readline().split()) 


		while True:
			line = f.readline()
			if not line: break
			key, value = line.split()
			self.icVal[key] = float(value)


	def getInformationContent(self, word):	
		if word not in self.icVal:
			return self.maxVal		
		return self.icVal[word]

	def printSortedList(self):
		sorted_list = sorted(self.icVal.items(), key=operator.itemgetter(1));
		# print(sorted_list)
		for pair in sorted_list:
			print(pair)

	# def printSortedValues(self):
	# 	newSort = sorted(self.sorting, key=lambda x: x[0])
	# 	for val in newSort:
	# 		print(val)
