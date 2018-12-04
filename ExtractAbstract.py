# import InformationContent as IC
from collections import defaultdict
from nltk.stem import WordNetLemmatizer
from lib import trimAbstract, trimAbstract_calculate, normalization, change
import csv
from nltk.corpus import stopwords 
import re


class ExtractAbstract:

	def __init__(self, FILENAME, IC, TFIDF,\
				ICThreshold, TFIDFThreshold):
		self.fileNum = 1
		self.FILENAME = FILENAME
		self.icValThreshold = ICThreshold
		self.tfidfValThreshold = TFIDFThreshold
		self.extractWordsToFile(self.FILENAME, IC, TFIDF)


	def extractWordsToFile(self, FILENAME,IC,TFIDF):
		stop_words = set(stopwords.words('english')) 
		to_sort = []

		with open(FILENAME, encoding="utf8", errors='ignore') as csvfile:
			f = csv.reader(csvfile, delimiter=',')
			next(f, None)
			for row in f:
				newFile = open("./abstracts/"+str(self.fileNum)+".txt", "w")		
				abstract = trimAbstract(row[7].split()); 
				lenAbstract = len(abstract)
				
				#extract significant words to sigWords using IC and TFIDF
				sigWords = []
				keywords = row[8].split('; ') + row[9].split('; ')
				
				for word in keywords:
					for k in word.split():
						changeK = change(k)
						if changeK not in sigWords:
							sigWords.append(changeK)

				for word in abstract:
					if word == '©' or re.match(r'\d{4}',word):
						break
					
					find_word = change(word)
					tfidfVal =  TFIDF.getTFIDF(self.fileNum, find_word)
					icVal = IC.getInformationContent(find_word) 
					normTfidfVal = normalization(TFIDF.maxVal, TFIDF.minVal, tfidfVal)
					normICVal = normalization(IC.maxVal, IC.minVal, icVal)
					to_sort.append((word, normTfidfVal,normICVal))
					if (word in stop_words) or (word in sigWords):
						continue
					elif (normICVal > self.icValThreshold) or \
						 (normICVal < self.icValThreshold and normTfidfVal>self.tfidfValThreshold): 
						sigWords.append(word)

				#store in file
				newFile.write(' '.join(sigWords))
				# print(' '.join(sigWords))
				# print('\n\n')
				newFile.close()
				self.fileNum += 1

		# print(to_sort)
		# print("word\t\t\tTFIDF\t\tIC")
		# sorted_list = sorted(to_sort, key = lambda k: k[1])
		# for k in sorted_list:
		# 	print(k)

		#View sorted value of IC
		# IC.printSortedValues();
