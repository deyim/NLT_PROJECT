# import InformationContent as IC
from collections import defaultdict
from nltk.stem import WordNetLemmatizer
from lib import trimAbstract, normalization
import csv
from nltk.corpus import stopwords 

def extractWordsToFile(FILENAME,IC,TFIDF):
	fileNum = 1
	tfidfValThreshold = 0.2
	icValThreshold = 0.4
	diffThreshold = 0.2
	stop_words = set(stopwords.words('english')) 

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
				if word == '©':
					break
				tfidfVal =  TFIDF.getTFIDF(fileNum, word)
				icVal = IC.getInformationContent(word) 
				normTfidfVal = normalization(TFIDF.maxVal, TFIDF.minVal, tfidfVal)
				normICVal = normalization(IC.maxVal, IC.minVal, icVal)
				if word in stop_words:
					continue
				if normICVal > icValThreshold or (normTfidfVal - normICVal) > diffThreshold: 
				# if normICVal > icValThreshold:
					sigWords.append(word)

		#store in file
		# newFile.write(title)
			newFile.write(' '.join(sigWords))
			print(' '.join(sigWords))
			print('\n\n')
			newFile.close()
			fileNum += 1

	#View sorted value of IC
	# IC.printSortedValues();
