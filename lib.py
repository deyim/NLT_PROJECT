import urllib.request
import json
import time
import re, string, unicodedata
import nltk
from nltk import word_tokenize, sent_tokenize

from nltk.stem import WordNetLemmatizer

def trimAbstract_calculate(abstract):
	lenAbstract = len(abstract)
	lemmatizer = WordNetLemmatizer()
	table = str.maketrans('', '', string.punctuation)
	for i in range(lenAbstract):
		abstract[i] = abstract[i].lower()
		abstract[i] = abstract[i].translate(table)
		abstract[i] = lemmatizer.lemmatize(abstract[i])
		# if abstract[i][-1] in ['.', ',', ':', ';', '?', '!', '\'']:
		# 	abstract[i] = abstract[i][:-1]
		# if abstract[i][-2:] == '\'s':
		# 	abstract[i] = abstract[i][:-2]

	return abstract

def trimAbstract(abstract):
	lenAbstract = len(abstract)
	lemmatizer = WordNetLemmatizer()
	table = str.maketrans('', '', string.punctuation)
	for i in range(lenAbstract):
		abstract[i] = abstract[i].lower()
		abstract[i] = abstract[i].translate(table)
		# abstract[i] = lemmatizer.lemmatize(abstract[i])
		# if abstract[i][-1] in ['.', ',', ':', ';', '?', '!', '\'']:
		# 	abstract[i] = abstract[i][:-1]
		# if abstract[i][-2:] == '\'s':
		# 	abstract[i] = abstract[i][:-2]

	return abstract

def normalization(maxVal, minVal, value):
	return ((value - minVal) / (maxVal - minVal))