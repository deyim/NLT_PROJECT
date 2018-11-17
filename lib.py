from nltk.stem import WordNetLemmatizer

def trimAbstract(abstract):
	lenAbstract = len(abstract)
	lemmatizer = WordNetLemmatizer()
	for i in range(lenAbstract):
		abstract[i] = abstract[i].lower()
		if abstract[i][-1] in ['.', ',', ':', ';', '?', '!', '\'']:
			abstract[i] = abstract[i][:-1]
		if abstract[i][-2:] == '\'s':
			abstract[i] = abstract[i][:-2]
		abstract[i] = lemmatizer.lemmatize(abstract[i])

	return abstract

def normalization(maxVal, minVal, value):
	return ((value - minVal) / (maxVal - minVal))