
import math
from collections import defaultdict

class TFIDF:
	corpusDict = defaultdict(int)
	paperNum = 0
	unavailableWordValue = 0.1

	def __init__(self, CORPUSFILE):
		"""
			for each word in every abstract of the corpus
			calculate number of documents with the word in it 
		"""
		f = open(CORPUSFILE, "r")
		while True:
			title = f.readline()
			if not title: break
			self.paperNum += 1
			documentDict = defaultdict(bool)
			f.readline(); f.readline() #delete blank lines
			abstract = f.readline().split()[1:-4]; f.readline()

			for word in abstract:
				lowerWord = word.lower()
				if lowerWord[-1] in ['.', ',', ':', ';', '?', '!', '\'']:
					lowerWord = lowerWord[:-1]
				documentDict[lowerWord] = True
				
			for word in documentDict:
				self.corpusDict[word] += 1

			documentDict.clear()

	def getTF(self,abstract,lenAbstract):
		abstractDict = defaultdict(int)
		ret = {}

		for word in abstract:
			abstractDict[word] += 1

		for word in abstractDict:
			ret[word] = abstractDict[word]/lenAbstract

		return ret

	def getIDF(self,word):
		if word not in self.corpusDict:
			return self.unavailableWordValue
		return math.log(self.paperNum /self.corpusDict[word]) 



























