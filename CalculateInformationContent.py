import random
import math
import pandas as pd
import csv
from collections import defaultdict
from lib import trimAbstract_calculate

FREQFILE = "./source/freqs.txt"
# FILENAME = "./source/corpus.txt"
# FILENAME = "./source/corpus.csv"
FILENAME = "./source/corpus.csv"
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



# f = open(FILENAME, "r")
# f = pd.read_csv(FILENAME, header=[7])

with open(FILENAME, encoding="utf8", errors='ignore') as csvfile:
	f = csv.reader(csvfile, delimiter=',')
	next(f, None)
	for row in f:
		# print(row[7])
		abstract = trimAbstract_calculate(row[7].split())
		lenAbstract = len(abstract);
		for word in abstract:				
			if word not in freqDic:
				continue
			icVal[word] = math.log(freqDic[word] / sumFreq,10) * (-1)
			maxVal = max(maxVal, icVal[word])
			minVal = min(minVal, icVal[word])

# f.close()


icF = open(ICFILE, "w")
icF.write(str(minVal) + " " + str(maxVal)+"\n")
for (key, value) in icVal.items():
	icF.write(key + " " + str(value)+"\n")
icF.close()










