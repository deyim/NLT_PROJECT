# import InformationContent as IC
from collections import defaultdict
from nltk.stem import WordNetLemmatizer
from lib import trimAbstract, normalization


def extractWordsToFile(FILENAME,IC,TFIDF):
	fileNum = 1
	f = open(FILENAME, "r")
	lemmatizer = WordNetLemmatizer()
	tfidfValThreshold = 0.5
	icValThreshold = 0.5
	diffThreshold = 0.2

	while True:
		title = f.readline()
		if not title: break
		newFile = open("./results/"+str(fileNum)+".txt", "w")		
		f.readline(); f.readline() # delete blank lines
		abstract = trimAbstract(f.readline().split()[1:-4]); lenAbstract = len(abstract) ; f.readline()
		
		#extract significant words to sigWords using IC and TFIDF
		sigWords = []

		#use both TFIDF value and IC value
		for word in abstract:
			tfidfVal =  TFIDF.getTFIDF(fileNum, word)
			icVal = IC.getInformationContent(word) 
			normTfidfVal = normalization(TFIDF.maxVal, TFIDF.minVal, tfidfVal)
			normICVal = normalization(IC.maxVal, IC.minVal, icVal)

			# if abs(normICVal - normTfidfVal) > 0.2:
			# 	print(fileNum, word)
			# 	print(tfidfVal, icVal)
			# 	print(normTfidfVal, normICVal)
			# 	print(abs(normICVal - normTfidfVal))


			# print(word, normICVal, normTfidfVal, (normICVal - normTfidfVal))
			if normICVal > icValThreshold or (normTfidfVal - normICVal) > diffThreshold: 
				sigWords.append(word)

		#store in file
		newFile.write(title)
		newFile.write(' '.join(sigWords))
		newFile.close()
		fileNum += 1

	#View sorted value of IC
	# IC.printSortedValues();
