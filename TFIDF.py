
import math
from collections import defaultdict
from nltk.stem import WordNetLemmatizer
from lib import trimAbstract

class TFIDF:
	tfidfVal = dict()
	corpusDict = defaultdict(int)

	paperNum = 0
	unavailableWordValue = 0.013513719166722855
	maxVal = -10000
	minVal = 10000

	def __init__(self, CORPUSFILE):
		"""
			for each word in every abstract of the corpus
			calculate number of documents with the word in it 
		"""
		f = open(CORPUSFILE, "r")
		lemmatizer = WordNetLemmatizer()
		while True:
			title = f.readline()
			if not title: break
			self.paperNum += 1
			documentDict = defaultdict(bool)
			f.readline(); f.readline() #delete blank lines
			abstract = trimAbstract(f.readline().split()[1:-4]); f.readline()
			lenAbstract = len(abstract)

			for word in abstract:
				documentDict[word] = True
				
			for word in documentDict:
				self.corpusDict[word] += 1

			documentDict.clear()

		f.close()

		thisPaper = 0
		f = open(CORPUSFILE, "r")
		while True:
			title = f.readline()
			if not title: break
			thisPaper += 1
			documentDict = defaultdict(bool)
			f.readline(); f.readline() #delete blank lines
			abstract = trimAbstract(f.readline().split()[1:-4]); lenAbstract = len(abstract) ;f.readline()


			TF = self.getTF(abstract, lenAbstract)

			for word in abstract:
				idfVal = math.log(self.paperNum /self.corpusDict[word]) 
				self.tfidfVal[(thisPaper, word)] = idfVal * TF[word]
				# if word == 'model':
					# print(self.paperNum, self.corpusDict[word])
					# print(word, idfVal, TF[word], self.tfidfVal[(thisPaper, word)])
				self.maxVal = max(self.maxVal, self.tfidfVal[(thisPaper, word)] )
				self.minVal = min(self.minVal, self.tfidfVal[(thisPaper, word)] )
		f.close()
		# print(self.maxVal, self.minVal)





	def getTF(self,abstract,lenAbstract):
		abstractDict = defaultdict(int)
		ret = {}

		for word in abstract:
			abstractDict[word] += 1

		for word in abstractDict:
			ret[word] = abstractDict[word]/lenAbstract

		return ret

	def getTFIDF(self,fileNum, word):
		if word not in self.corpusDict:
			return self.minVal

		return self.tfidfVal[(fileNum, word)]



























