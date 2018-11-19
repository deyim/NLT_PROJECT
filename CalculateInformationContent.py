import random
import math
from collections import defaultdict
from lib import trimAbstract

FREQFILE = "./source/freqs.txt"
FILENAME = "./source/corpus.txt"
ICFILE = "./source/ic.txt"
icVal = dict()
freqDic = {}
sumFreq = 0
sorting = []
maxVal = -10000
minVal = 10000

freq = open(FREQFILE,"r")
while True:
	line = freq.readline()
	if not line: break

	oneLine = line.split()
	freqDic[oneLine[0]] = int(oneLine[1])
	sumFreq += int(oneLine[1])	



f = open(FILENAME, "r")
while True:
	title = f.readline()
	if not title: break
	f.readline(); f.readline()
	abstract = trimAbstract(f.readline().split()[1:-4]); lenAbstract = len(abstract) ; f.readline()
	

	for word in abstract:				
		if word not in freqDic:
			continue
		icVal[word] = math.log(freqDic[word] / sumFreq,10) * (-1)
		maxVal = max(maxVal, icVal[word])
		minVal = min(minVal, icVal[word])

f.close()


icF = open(ICFILE, "w")
icF.write(str(minVal) + " " + str(maxVal)+"\n")
for (key, value) in icVal.items():
	icF.write(key + " " + str(value)+"\n")
icF.close()










