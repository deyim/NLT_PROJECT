import urllib.request
import json
import time
import re, string, unicodedata
import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.stem import LancasterStemmer, WordNetLemmatizer

start = time.time()
ids = []
queryList = ['artificial%20intelligence', 'neural%20network', 'machine%20learning',\
			'deep%20learning', 'natural%20language%20processing', 'supervised%20learning',\
			'unsupervised%20learning', 'predictive%20analytics', 'classification%20clustering'\
			'data%20analysis','data%20analytics', 'computer%20vision']
# queryList = ['artificial%20intelligence', 'neural%20network']

for query in queryList:
	f = open("CORE_Corpus.txt","a")
	for page in range(1,101):
	# for page in range(1,2):
		url = 'https://core.ac.uk:443/api-v2/articles/search/'+query+'?page='+str(page)+'&pageSize=100&metadata=true&fulltext=true&apiKey=2eHwu9QPcIgMW3OGKVsjR08lxnUfCrNL'
		with urllib.request.urlopen(url) as response:
		    resp = response.read()
		result_as_json = json.loads(resp.decode('utf-8'))
		
		for paper in result_as_json['data']:
			paperId = paper['id']
			if paperId not in ids:
				ids.append(paperId)
			for line in paper['fullText'].split('\n'):
				if line == 'References' or line == 'REFERENCES':
					break
				line = re.sub(r'\([^)]*\)','',line)
				line = re.sub(r'[^\x41-\x5A\x61-\x7A]',' ', line)
				tokens = word_tokenize(line)
				tokens = [w.lower() for w in tokens]
				table = str.maketrans('', '', string.punctuation)
				stripped = [w.translate(table) for w in tokens]
				words = [w for w in stripped if w == 'a' or len(w) > 1]
				if len(words) < 3: continue

				f.write(' '.join(words))
				f.write(' ')



		if page % 20 == 0:
			end = time.time()
			print(query, page, end - start)

	f.close()

meta = open("meta.txt","w")
meta.write(str(len(ids)))
meta.write('\n')
meta.write(str(' '.join(ids)))
meta.close()
