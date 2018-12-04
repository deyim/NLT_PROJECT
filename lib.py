import urllib.request
import json
import time
import re, string, unicodedata
import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords 

from nltk.stem import WordNetLemmatizer

def change(word):
	lemmatizer = WordNetLemmatizer()
	table = str.maketrans('', '', string.punctuation)
	word = word.lower().translate(table)
	word = lemmatizer.lemmatize(word)
	return word

def trimAbstract_calculate(abstract):
	lenAbstract = len(abstract)
	lemmatizer = WordNetLemmatizer()
	table = str.maketrans('', '', string.punctuation)

	newAbstract = []
	for word in abstract:
		if '-' in word:
			# print(word)
			for k in word.split('-'):
				newAbstract.append(k)
		else:
			newAbstract.append(word)
	abstract = newAbstract


	
	for i in range(lenAbstract):
		abstract[i] = abstract[i].lower()
		abstract[i] = abstract[i].translate(table)
		abstract[i] = lemmatizer.lemmatize(abstract[i])
		if abstract[i] and abstract[i][-1] in ['.', ',', ':', ';', '?', '!', '\'']:
			abstract[i] = abstract[i][:-1]
		# if abstract[i][-2:] == '\'s':
		# 	abstract[i] = abstract[i][:-2]

	return abstract

def trimAbstract(abstract):
	lenAbstract = len(abstract)
	lemmatizer = WordNetLemmatizer()
	table = str.maketrans('', '', string.punctuation)
	# stop_words = set(stopwords.words('english')) 

	newAbstract = []
	for word in abstract:
		if '-' in word:
			# print(word)
			for k in word.split('-'):
				newAbstract.append(k)
		else:
			newAbstract.append(word)
	abstract = newAbstract

	for i in range(lenAbstract):
		abstract[i] = abstract[i].lower()
		abstract[i] = abstract[i].translate(table)
		# if abstract[i] in stop_words:
		# abstract[i] = lemmatizer.lemmatize(abstract[i])
		if abstract[i] and abstract[i][-1] in ['.', ',', ':', ';', '?', '!', '\'']:
			abstract[i] = abstract[i][:-1]
		# if abstract[i][-2:] == '\'s':
		# 	abstract[i] = abstract[i][:-2

	return abstract

def normalization(maxVal, minVal, value):
	# print("TFIDF")
	# print(maxVal, minVal, value)
	# print(value-minVal)
	# print(maxVal-minVal)
	# print(((value - minVal) / (maxVal - minVal)))
	return ((value - minVal) / (maxVal - minVal))