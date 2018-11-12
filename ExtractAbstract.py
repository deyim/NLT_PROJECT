# import InformationContent as IC
from collections import defaultdict
from nltk.stem import WordNetLemmatizer


def extractWordsToFile(FILENAME,IC,TFIDF):
	fileNum = 1
	f = open(FILENAME, "r")
	lemmatizer = WordNetLemmatizer()

	while True:
		title = f.readline()
		if not title: break
		newFile = open("./results/"+str(fileNum)+".txt", "w")		
		f.readline(); f.readline() # delete blank lines
		abstract = f.readline().split()[1:-4]; lenAbstract = len(abstract) ; f.readline()
		
		#extract significant words to sigWords using IC and TFIDF
		sigWords = []

		#trim words
		for i in range(lenAbstract):
			abstract[i] = abstract[i].lower()
			if abstract[i][-1] in ['.', ',', ':', ';', '?', '!', '\''] or \
				abstract[i][-2:] in ['\'s']:
				abstract[i] = abstract[i][:-1]
			abstract[i] = lemmatizer.lemmatize(abstract[i])

		#get TF as dictionary
		TF = TFIDF.getTF(abstract, lenAbstract)

		#use both TFIDF value and IC value
		for word in abstract:
			tfidfVal =  TF[word] * TFIDF.getIDF(word)
			icVal = IC.getInformationContent(word) 
			# print(word, tfidfVal, icVal)
			if tfidfVal < 0.03: continue
			if icVal > 2 and word not in sigWords:
				sigWords.append(word)

		#store in file
		newFile.write(title)
		newFile.write(' '.join(sigWords))
		newFile.close()
		fileNum += 1

	#View sorted value of IC
	# IC.printSortedValues();
