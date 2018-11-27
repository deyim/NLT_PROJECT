
import math
from collections import defaultdict
from nltk.stem import WordNetLemmatizer
from lib import trimAbstract

class TFIDF:
	tfidfVal = dict()

	def __init__(self, FILENAME):
		f = open(FILENAME, "r")
		self.minVal, self.maxVal = map(float, f.readline(0.split())) 

		while True:
			line = f.readline()
			if not line: break
			paperNum, word, value = line.split()
			self.tfidfVal[(int(paperNum), word)] = float(value)

	

	def getTFIDF(self,fileNum, word):
		if word not in self.tfidfVal:
			return self.minVal

		return self.tfidfVal[(fileNum, word)]



























