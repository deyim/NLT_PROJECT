import ExtractAbstract
from InformationContent import InformationContent
from TFIDF import TFIDF as TFIDF


if __name__ == "__main__":

	# Calculate IC and TFIDF
	IC = InformationContent("./source/freqs.txt", "./source/corpus.txt")
	TfIdf = TFIDF("./source/corpus.txt")

	# Use IC and TFIDF to extract words from abstracts
	ExtractAbstract.extractWordsToFile("./source/corpus.txt", IC, TfIdf)
	
	