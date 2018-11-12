import random
import math


class InformationContent:
	freqDic = {}
	sumFreq = 0
	sorting = []
	def __init__(self, FREQFILE):
		freq = open(FREQFILE,"r")
		while True:
			line = freq.readline()
			if not line: break

			oneLine = line.split()
			self.freqDic[oneLine[0]] = int(oneLine[1])
			self.sumFreq += int(oneLine[1])		


	def getInformationContent(self, word):
		if word not in self.freqDic:
			return 10
		value = math.log(self.freqDic[word] / self.sumFreq,10) * (-1)
		self.sorting.append((value,word))
		
		return value

	def printSortedValues(self):
		newSort = sorted(self.sorting, key=lambda x: x[0])
		for val in newSort:
			print(val)
