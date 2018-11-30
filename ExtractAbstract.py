# import InformationContent as IC
from collections import defaultdict
from nltk.stem import WordNetLemmatizer
from lib import trimAbstract, normalization
import csv

def extractWordsToFile(FILENAME,IC,TFIDF):
	fileNum = 1
	tfidfValThreshold = 0.5
	icValThreshold = 0.5
	diffThreshold = 0.2

	with open(FILENAME, encoding="utf8", errors='ignore') as csvfile:
		f = csv.reader(csvfile, delimiter=',')
		next(f, None)
		for row in f:
			newFile = open("./results/"+str(fileNum)+".txt", "w")		
			abstract = trimAbstract(row[7].split()); 
			lenAbstract = len(abstract)
			
			#extract significant words to sigWords using IC and TFIDF
			sigWords = []

			#use both TFIDF value and IC value
			for word in abstract:
				tfidfVal =  TFIDF.getTFIDF(fileNum, word)
				icVal = IC.getInformationContent(word) 
				normTfidfVal = normalization(TFIDF.maxVal, TFIDF.minVal, tfidfVal)
				normICVal = normalization(IC.maxVal, IC.minVal, icVal)
				
				if normICVal > icValThreshold or (normTfidfVal - normICVal) > diffThreshold: 
					sigWords.append(word)

		#store in file
		# newFile.write(title)
			newFile.write(' '.join(sigWords))
			newFile.close()
			fileNum += 1

	#View sorted value of IC
	# IC.printSortedValues();
