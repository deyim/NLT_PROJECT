import urllib.request
import json
import time
import re, string, unicodedata
import nltk
from nltk import word_tokenize, sent_tokenize

initial_start = time.time()
ids = []
queryList = ['artificial%20intelligence', 'neural%20network', 'machine%20learning',\
			'deep%20learning', 'natural%20language%20processing', 'supervised%20learning',\
			'unsupervised%20learning', 'predictive%20analytics', 'classification%20clustering',\
			'data%20analysis','data%20analytics', 'computer%20vision']
keys = ['2eHwu9QPcIgMW3OGKVsjR08lxnUfCrNL', 'wsxAHgpaCL938o4ydjt0IiVDJzFW756n','82pXuVgHNAIdJ6SWFLwGrahYZ7niDvPe',\
		'K8V16NwY0AgPEkTrhpxvltZQoH9sy5nI', 'FaxpJtMy659ImAogYSXuib03NUnEeVQK', 'NG6IWVPeA3SK7HY4CwMOmg8EtFL5cJz2',\
		'SMElezHLsgqw4nZ5ijvCo9WO2GY8b1FV']
# queryList = ['neural%20network']
# q = 0
# idf = open("paper_ids.txt","r")

f = open('CORE_Corpus_final.txt',"w")
f.close()

for query in queryList:
	f = open("CORE_Corpus_final.txt","a")
	# for page in range(41,101):
	for page in range(1,101):
		loop_start = time.time()
		# params = urllib.urlencode({})
		url = 'https://core.ac.uk:443/api-v2/articles/search/'+query+'?page='+str(page)+'&pageSize=100&metadata=true&fulltext=true&apiKey='+keys[page%7]
		print(url)
		resp = None
		try:
			response = urllib.request.urlopen(url)
			try:
				resp = response.read()
			except:				
				print("RESPONSE READING ERROR OCCURRED")
				time.sleep(15)
				print("sleeping for a while")
				continue
		except:
			print("URL REQUEST FAILED")
			continue
		

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
				#John Speaks Korean => ['John', 'Speaks.', 'Korean']
				tokens = [w.lower() for w in tokens]

				table = str.maketrans('', '', string.punctuation)
				stripped = [w.translate(table) for w in tokens]
				words = [w for w in stripped if w == 'a' or len(w) > 1]
				if len(words) < 3: continue

				f.write(' '.join(words))
				f.write(' ')

		loop_end = time.time()
		print(query, page, loop_end - loop_start)
		if loop_end - loop_start < 10:
			time.sleep(11-(loop_end-loop_start))

		if page % 5 == 0:
			end = time.time()
			print(query, page, end - initial_start)

	f.close()

meta = open("meta.txt","w")
meta.write(str(len(ids)))
meta.write('\n')
meta.write(str(' '.join(ids)))
meta.close()
