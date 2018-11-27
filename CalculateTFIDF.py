
import math
from collections import defaultdict
from lib import trimAbstract

def getTF(abstract,lenAbstract):
	abstractDict = defaultdict(int)
	ret = {}

	for word in abstract:
		abstractDict[word] += 1

	for word in abstractDict:
		ret[word] = abstractDict[word]/lenAbstract

	return ret

CORPUSFILE = "./source/corpus.txt"
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
f = open(CORPUSFILE, "r")

while True:
	title = f.readline()
	if not title: break
	paperNum += 1
	documentDict = defaultdict(bool)
	f.readline(); f.readline() #delete blank lines
	abstract = trimAbstract(f.readline().split()[1:-4]); f.readline()
	lenAbstract = len(abstract)

	for word in abstract:
		documentDict[word] = True
		
	for word in documentDict:
		corpusDict[word] += 1

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


	TF = getTF(abstract, lenAbstract)

	for word in abstract:
		idfVal = math.log(paperNum /corpusDict[word]) 
		tfidfVal[(thisPaper, word)] = idfVal * TF[word]
		maxVal = max(maxVal, tfidfVal[(thisPaper, word)] )
		minVal = min(minVal, tfidfVal[(thisPaper, word)] )
f.close()

tfidfF = open(TFIDFFILE, "w")
tfidfF.write(str(minVal) + " " + str(maxVal)+"\n")
for (key, value) in tfidfVal.items():
	tfidfF.write(str(key[0])+" "+str(key[1]) + " " + str(value)+"\n")
tfidfF.close()

