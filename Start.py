import ExtractAbstract
from InformationContent import InformationContent
from TFIDF import TFIDF as TFIDF


if __name__ == "__main__":

	# Calculate IC and TFIDF
	IC = InformationContent("./source/ic.txt")
	# IC.printSortedList()
	TfIdf = TFIDF("./source/tfidf.txt")
	# TfIdf.printSortedList()

	# Use IC and TFIDF to extract words from abstracts
	ExtractAbstract.extractWordsToFile("./source/corpus.csv", IC, TfIdf)
	
	