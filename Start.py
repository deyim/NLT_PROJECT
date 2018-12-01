import ExtractAbstract
from InformationContent import InformationContent
from TFIDF import TFIDF as TFIDF


if __name__ == "__main__":

	# Calculate IC and TFIDF
	IC = InformationContent("./source/ic.txt")
	TfIdf = TFIDF("./source/tfidf.txt")

	# Use IC and TFIDF to extract words from abstracts
	ExtractAbstract.extractWordsToFile("./source/corpus_tmp.csv", IC, TfIdf)
	
	