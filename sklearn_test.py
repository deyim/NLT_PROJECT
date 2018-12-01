# with open(vectors_part.txt) as f:
from sklearn import metrics
# lines = [line.rstrip('\n') for line in ('vectors_part.txt')]

f = open('vectors_part.txt','r+')
wv = []
while True:
	line = f.readline()
	if not line:
		break
	line = line.split()
	word = line[0]
	vector = [float(comp) for comp in line[1:]]
	wv.append((word,vector))
	
print(wv[0][0], wv[3][0])
print(metrics.pairwise.cosine_similarity([wv[0][1]],[wv[3][1]]))

# message = f.readlines()
# print (message)
f.close()