import csv
import math
from collections import defaultdict
from lib import trimAbstract_calculate


def getTF(abstract,lenAbstract):
	abstractDict = defaultdict(int)
	ret = {}

	for word in abstract:
		abstractDict[word] += 1

	for word in abstractDict:
		ret[word] = abstractDict[word]/lenAbstract

	return ret

# CORPUSFILE = "./source/corpus.csv"
CORPUSFILE = "./source/corpus5.csv"
TFIDFFILE = "./source/tfidf.txt"


tfidfVal = dict()
corpusDict = defaultdict(int)
paperNum = 0
maxVal = -10000
minVal = 10000

"""
	for each word in every abstract of the corpus
	calculate number of documents with the word in it 
"""

with open(CORPUSFILE, encoding="utf8", errors='ignore') as csvfile:
	f = csv.reader(csvfile, delimiter=',')
	next(f,None)
	
	documentDict = defaultdict(bool)
	for row in f:
		paperNum += 1
		abstract = trimAbstract_calculate(row[7].split())
		
		for word in abstract:
			documentDict[word] = True	
		# print(documentDict)		
		for word in documentDict:
			corpusDict[word] += 1

		documentDict.clear()

# f.close()
# print(corpusDict)

thisPaper = 0
with open(CORPUSFILE, encoding="utf8", errors='ignore') as csvfile:
	f = csv.reader(csvfile, delimiter=',')
	next(f,None)
	
	documentDict = defaultdict(bool)
	for row in f:
		thisPaper += 1
		abstract = trimAbstract_calculate(row[7].split()); 
		lenAbstract = len(abstract) 

		TF = getTF(abstract, lenAbstract)

		for word in abstract:
			idfVal = math.log(paperNum /corpusDict[word]) 
			# print(paperNum, corpusDict[word], idfVal, TF[word])
			tfidfVal[(thisPaper, word)] = idfVal * TF[word]
			maxVal = max(maxVal, tfidfVal[(thisPaper, word)] )
			minVal = min(minVal, tfidfVal[(thisPaper, word)] )
# f.close()

tfidfF = open(TFIDFFILE, "w")
tfidfF.write(str(minVal) + " " + str(maxVal)+"\n")
for (key, value) in tfidfVal.items():
	tfidfF.write(str(key[0])+" "+str(key[1]) + " " + str(value)+"\n")
tfidfF.close()

