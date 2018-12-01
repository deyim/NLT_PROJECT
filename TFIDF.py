import operator
import math
from collections import defaultdict
from nltk.stem import WordNetLemmatizer
from lib import trimAbstract

class TFIDF:
	tfidfVal = dict()

	def __init__(self, FILENAME):
		f = open(FILENAME, "r")
		self.minVal, self.maxVal = map(float, f.readline().split()) 

		while True:
			line = f.readline()
			if not line: break
			# print(line)
			try:
				paperNum, word, value = line.split()
			except:
				continue
			self.tfidfVal[(int(paperNum), word)] = float(value)

	

	def getTFIDF(self,fileNum, word):
		if (int(fileNum), word) not in self.tfidfVal:
			return self.minVal

		return self.tfidfVal[(fileNum, word)]

	def printSortedList(self):
		sorted_list = sorted(self.tfidfVal.items(), key=operator.itemgetter(1));
		# print(sorted_list)
		for pair in sorted_list:
			print(pair)



























