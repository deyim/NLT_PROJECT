# import InformationContent as IC
from collections import defaultdict
from nltk.stem import WordNetLemmatizer
from lib import trimAbstract, trimAbstract_calculate, normalization, change
import csv
from nltk.corpus import stopwords 
import re

def extractWordsToFile(FILENAME,IC,TFIDF):
	fileNum = 1
	tfidfValThreshold = 0.3
	icValThreshold = 0.35
	diffThreshold = 0.2
	stop_words = set(stopwords.words('english')) 

	"""
	Debuggin Code
	"""
	to_sort = []


	with open(FILENAME, encoding="utf8", errors='ignore') as csvfile:
		f = csv.reader(csvfile, delimiter=',')
		next(f, None)
		for row in f:
			newFile = open("./results/"+str(fileNum)+".txt", "w")		
			abstract = trimAbstract(row[7].split()); 
			lenAbstract = len(abstract)
			
			#extract significant words to sigWords using IC and TFIDF
			sigWords = []
			keywords1 = row[8].split('; ')
			keywords2 = row[9].split('; ')
			for word in keywords1:
				for k in word.split():
					changeK = change(k)
					if changeK not in sigWords:
						sigWords.append(changeK)

			for word in keywords2:
				for k in word.split():
					changeK = change(k)
					if changeK not in sigWords:
						sigWords.append(changeK)
			#use both TFIDF value and IC value

			for word in abstract:
				if word == '©' or re.match(r'\d{4}',word):
					break
				
				find_word = change(word)
				tfidfVal =  TFIDF.getTFIDF(fileNum, find_word)
				icVal = IC.getInformationContent(find_word) 
				normTfidfVal = normalization(TFIDF.maxVal, TFIDF.minVal, tfidfVal)
				normICVal = normalization(IC.maxVal, IC.minVal, icVal)
				to_sort.append((word, normTfidfVal,normICVal))
				# print(word, tfidfVal, icVal)
				# print(word, normTfidfVal, normICVal)
				# print(normICVal < icValThreshold and normTfidfVal )
				if (word in stop_words) or (word in sigWords):
					continue
				elif (normICVal > icValThreshold) or (normICVal < icValThreshold and normTfidfVal>tfidfValThreshold): 
				# if normICVal > icValThreshold and (word not in sigWords):
					# print(word)
					sigWords.append(word)

		#store in file
		# newFile.write(title)
			newFile.write(' '.join(sigWords))
			print(' '.join(sigWords))
			print('\n\n')
			newFile.close()
			fileNum += 1

	# print(to_sort)
	# print("word\t\t\tTFIDF\t\tIC")
	# sorted_list = sorted(to_sort, key = lambda k: k[1])
	# for k in sorted_list:
	# 	print(k)

	#View sorted value of IC
	# IC.printSortedValues();
