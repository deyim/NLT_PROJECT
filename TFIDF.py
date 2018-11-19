
import math
from collections import defaultdict
from nltk.stem import WordNetLemmatizer
from lib import trimAbstract

class TFIDF:
	tfidfVal = dict()

	def __init__(self, FILENAME):
		f = open(FILENAME, "r")
		vals = f.readline().split()
		self.minVal, self.maxVal = float(vals[0]), float(vals[1])


		while True:
			line = f.readline()
			if not line: break
			paperNum, word, value = line.split()
			self.tfidfVal[(int(paperNum), word)] = float(value)

	

	def getTFIDF(self,fileNum, word):
		if word not in self.tfidfVal:
			return self.minVal

		return self.tfidfVal[(fileNum, word)]



























