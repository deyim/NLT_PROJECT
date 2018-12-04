from ExtractAbstract import ExtractAbstract
from InformationContent import InformationContent

from TFIDF import TFIDF as TFIDF
from ClusterRelatedness import ClusterRelatedness
from DimensionRelatedness import DimensionRelatedness
from RelatednessGraph import RelatednessGraph

if __name__ == "__main__":

	'''
		PART 1 - 1
		Calculate IC and TFIDF
	'''
	IC = InformationContent("./source/ic.txt")
	#DEBUG: IC.printSortedList()
	TfIdf = TFIDF("./source/tfidf.txt")
	#DEBUG: TfIdf.printSortedList()


	'''
		PART 1 - 2
		Use IC and TFIDF to extract words from abstracts
	'''
	Extractor = ExtractAbstract("./source/corpus5.csv", IC, TfIdf, 0.35, 0.3) #IC THReshold / TFIDF Threst


	'''
		PART 2
		Calculate Relatedness
	'''
	# Finding Relatedness 1 - Find Vector Cluster
	# ClusterRelatedness = ClusterRelatedness("./source/vectors.txt", "./abstracts/", Extractor.fileNum)

	# Finding Relatedness 2 - Compare Word Pairs
	DimensionRelatedness = DimensionRelatedness("./source/vectors.txt", "./results/relatedness.txt", \
							"./abstracts/", Extractor.fileNum, 0.4)




	'''
		PART 3
	'''
	# Visualization

	# RelatednessGraph = RelatednessGraph(DimensionRelatedness.outfile)
	# RelatednessGraph = RelatednessGraph("./results/relatedness.txt")




	'''
	Debugging
	'''
	
	