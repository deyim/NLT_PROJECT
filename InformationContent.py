import random
import math
from collections import defaultdict
from nltk.stem import WordNetLemmatizer
from lib import trimAbstract

class InformationContent:
	icVal = dict()
	freqDic = {}
	sumFreq = 0
	sorting = []
	maxVal = -10000
	minVal = 10000

	def __init__(self, FREQFILE, FILENAME):
		
		freq = open(FREQFILE,"r")
		while True:
			line = freq.readline()
			if not line: break

			oneLine = line.split()
			self.freqDic[oneLine[0]] = int(oneLine[1])
			self.sumFreq += int(oneLine[1])	



		f = open(FILENAME, "r")
		while True:
			title = f.readline()
			if not title: break
			f.readline(); f.readline()
			abstract = trimAbstract(f.readline().split()[1:-4]); lenAbstract = len(abstract) ; f.readline()
			

			for word in abstract:				
				if word not in self.freqDic:
					continue
				self.icVal[word] = math.log(self.freqDic[word] / self.sumFreq,10) * (-1)
				self.maxVal = max(self.maxVal, self.icVal[word])
				self.minVal = min(self.minVal, self.icVal[word])

		# print(self.maxVal, self.minVal)


	def getInformationContent(self, word):
		if word not in self.freqDic:
			return self.maxVal
			
		# if word == 'with':
			# print(self.icVal)
		return self.icVal[word]

	def printSortedValues(self):
		newSort = sorted(self.sorting, key=lambda x: x[0])
		for val in newSort:
			print(val)
