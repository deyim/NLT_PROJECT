import ExtractAbstract
from InformationContent import InformationContent
from TFIDF import TFIDF as TFIDF


if __name__ == "__main__":

	# Calculate IC and TFIDF
	IC = InformationContent("./source/freqs.txt")
	TfIdf = TFIDF("./source/corpus.txt")

	# Use IC and TFIDF to extract words from abstracts
	ExtractAbstract.extractWordsToFile("./source/corpus.txt", IC, TfIdf)
	
	# model 0.030799688466358152 3.536644151539152
	# model 0.030799688466358152 3.536644151539152
	# model 0.013279575824263118 3.536644151539152
	'''
	model rnn rnn sequence representation representation sequence model sequence sequence rnn model model representation
	model rnn sequence representation
	'''