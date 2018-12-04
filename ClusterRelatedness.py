import math
import numpy as np 
from numpy import array
from sklearn.cluster import SpectralClustering
from sklearn import metrics
import matplotlib.pyplot as plt


from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

from scipy.cluster import  hierarchy
import silicon
from pyclustering.cluster import optics

import random;

from pyclustering.cluster import cluster_visualizer, cluster_visualizer_multidim;
from pyclustering.cluster.optics import optics, ordering_analyser, ordering_visualizer;


from pyclustering.utils import read_sample, timedcall;

# from pyclustering.samples.definitions import SIMPLE_SAMPLES, FCPS_SAMPLES;

class ClusterRelatedness:

	def __init__(self, VECTORFILE, DIR, FILENUM):
		self.DIR = DIR
		self.FILENUM = FILENUM
		self.vectors = self.getVectors(VECTORFILE)
		self.findRelatedness()

	def getVectors(self, VECTORFILE):
		v = open(VECTORFILE, 'r')
		wv = {}
		"""
			DEBUGGING
		"""
		i = 0

		while True:
			i+=1
			if i%100000==0: 
				print(i/100000)
			line = v.readline()
			if not line: break
			wordvec = line.split()
			word = wordvec[0]			
			# vector = array([float(comp) for comp in wordvec[1:]])
			vector = [float(comp) for comp in wordvec[1:]]
			wv[word] = vector

		print("GOT vectors from vectorfile")
		return wv

	def findRelatedness(self):
		# test set
		# self.pairRelatedness(1,2)
		for i in range(1,self.FILENUM):
			for j in range(1,self.FILENUM):
				print('relatedness',i,j)
				# if i==j: continue
				rel = self.pairRelatedness(i,j)

	def filterWords(self, words):
		newWords = []
		for word in words:
			if word not in self.vectors:
				continue
			newWords.append(word)
		return newWords 

	def pairRelatedness(self, i, j):
		P1 = open(self.DIR+str(i)+".txt")
		P2 = open(self.DIR+str(j)+".txt")
		p1Words = self.filterWords(P1.readline().split())
		p2Words = self.filterWords(P2.readline().split())
		P1.close(); P2.close()
		p1Vec = self.findVectorsOfWords(p1Words) 
		p2Vec = self.findVectorsOfWords(p2Words)


		met = self.findCosineSimMatrix(p1Vec, p2Vec, p1Words, p2Words)
		#OPTICS
		print("*********OPTICS", i, j, "*********")
		self.template_clustering(met, 0.1, 3);
		self.template_clustering(met, 0.12, 3);
		self.template_clustering(met, 0.14, 3);
		self.template_clustering(met, 0.16, 3);
		self.template_clustering(met, 0.2, 3);


		self.template_clustering(p1Vec+p2Vec, 0.001, 3);
		self.template_clustering(p1Vec+p2Vec, 0.002, 3);
		self.template_clustering(p1Vec+p2Vec, 0.003, 3);
		self.template_clustering(p1Vec+p2Vec, 0.004, 3);
		self.template_clustering(p1Vec+p2Vec, 0.005, 3);
		

		# COSINE DISTANCE MATRIX - DBSCAN
		# print("DBSCAN _ COSIM", i, j)
		# met = np.matrix(met)
		# clustering = DBSCAN(eps=5, min_samples=3).fit(met)

		# core_samples_mask = np.zeros_like(clustering.labels_, dtype=bool)
		# core_samples_mask[clustering.core_sample_indices_] = True
		# labels = clustering.labels_

		# n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
		# n_noise_ = list(labels).count(-1)
		# print(labels)
		# print('Estimated number of clusters: %d' % n_clusters_)
		# print('Estimated number of noise points: %d' % n_noise_)

		
		# clustering = DBSCAN(eps=6, min_samples=3).fit(met)

		# core_samples_mask = np.zeros_like(clustering.labels_, dtype=bool)
		# core_samples_mask[clustering.core_sample_indices_] = True
		# labels = clustering.labels_
		# print(labels)
		# n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
		# n_noise_ = list(labels).count(-1)
		# print('Estimated number of clusters: %d' % n_clusters_)
		# print('Estimated number of noise points: %d' % n_noise_)


		# clustering = DBSCAN(eps=7, min_samples=3).fit(met)

		# core_samples_mask = np.zeros_like(clustering.labels_, dtype=bool)
		# core_samples_mask[clustering.core_sample_indices_] = True
		# labels = clustering.labels_
		# print(labels)
		# n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
		# n_noise_ = list(labels).count(-1)
		# print('Estimated number of clusters: %d' % n_clusters_)
		# print('Estimated number of noise points: %d' % n_noise_)
		# stscalar = StandardScaler().fit(met)
		# met = stscalar.transform(met)


		# threshold = 0.025
		# Z = hierarchy.linkage(met,"average", metric="cosine")
		# C = hierarchy.fcluster(Z, threshold, criterion="distance")
		# print('%d unique clusters '%(len(np.unique(C))))

		# threshold = 0.02
		# Z = hierarchy.linkage(met,"average", metric="cosine")
		# C = hierarchy.fcluster(Z, threshold, criterion="distance")
		# print('%d unique clusters '%(len(np.unique(C))))

		# threshold = 0.015
		# Z = hierarchy.linkage(met,"average", metric="cosine")
		# C = hierarchy.fcluster(Z, threshold, criterion="distance")
		# print('%d unique clusters '%(len(np.unique(C))))

		# threshold = 0.01
		# Z = hierarchy.linkage(met,"average", metric="cosine")
		# C = hierarchy.fcluster(Z, threshold, criterion="distance")
		# print('%d unique clusters '%(len(np.unique(C))))


		# clustering = DBSCAN(eps=0.6, min_samples=3).fit(met)
		# print(clustering)
		# core_samples_mask = np.zeros_like(clustering.labels_, dtype=bool)
		# core_samples_mask[clustering.core_sample_indices_] = True
		# labels = clustering.labels_

		# Number of clusters in labels, ignoring noise if present.
		# n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
		# n_noise_ = list(labels).count(-1)
		# print('Estimated number of clusters: %d' % n_clusters_)
		# print('Estimated number of noise points: %d' % n_noise_)


		# print('clustering lables:', clustering.labels_)
		# print('clustering components:', clustering.components_)
		# print('clustering indices:', clustering.core_sample_indices_)

		# COSINE DISTANCE MATRIX - DBSCAN
		print("DBSCAN _ VECTORS", i, j)

		met = p1Vec + p2Vec
		met = np.matrix(met)
		# c = silicon.CosineClustering(met, sim_threshold = )
		# stscalar = StandardScaler().fit(met)
		# met = stscalar.transform(met)

		# clustering = DBSCAN(eps=5, min_samples=3).fit(met)

		# core_samples_mask = np.zeros_like(clustering.labels_, dtype=bool)
		# core_samples_mask[clustering.core_sample_indices_] = True
		# labels = clustering.labels_

		# n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
		# n_noise_ = list(labels).count(-1)
		# print(labels)
		# print('Estimated number of clusters: %d' % n_clusters_)
		# print('Estimated number of noise points: %d' % n_noise_)

		
		# clustering = DBSCAN(eps=6, min_samples=3).fit(met)

		# core_samples_mask = np.zeros_like(clustering.labels_, dtype=bool)
		# core_samples_mask[clustering.core_sample_indices_] = True
		# labels = clustering.labels_
		# print(labels)
		# n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
		# n_noise_ = list(labels).count(-1)
		# print('Estimated number of clusters: %d' % n_clusters_)
		# print('Estimated number of noise points: %d' % n_noise_)


		# clustering = DBSCAN(eps=7, min_samples=3).fit(met)

		# core_samples_mask = np.zeros_like(clustering.labels_, dtype=bool)
		# core_samples_mask[clustering.core_sample_indices_] = True
		# labels = clustering.labels_
		# print(labels)
		# n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
		# n_noise_ = list(labels).count(-1)
		# print('Estimated number of clusters: %d' % n_clusters_)
		# print('Estimated number of noise points: %d' % n_noise_)


		# clustering = DBSCAN(eps=5, min_samples=2).fit(met)

		# core_samples_mask = np.zeros_like(clustering.labels_, dtype=bool)
		# core_samples_mask[clustering.core_sample_indices_] = True
		# labels = clustering.labels_

		# n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
		# n_noise_ = list(labels).count(-1)
		# print('Estimated number of clusters: %d' % n_clusters_)
		# print('Estimated number of noise points: %d' % n_noise_)

		
		# clustering = DBSCAN(eps=6, min_samples=2).fit(met)

		# core_samples_mask = np.zeros_like(clustering.labels_, dtype=bool)
		# core_samples_mask[clustering.core_sample_indices_] = True
		# labels = clustering.labels_

		# n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
		# n_noise_ = list(labels).count(-1)
		# print('Estimated number of clusters: %d' % n_clusters_)
		# print('Estimated number of noise points: %d' % n_noise_)


		# clustering = DBSCAN(eps=7, min_samples=2).fit(met)

		# core_samples_mask = np.zeros_like(clustering.labels_, dtype=bool)
		# core_samples_mask[clustering.core_sample_indices_] = True
		# labels = clustering.labels_

		# n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
		# n_noise_ = list(labels).count(-1)
		# print('Estimated number of clusters: %d' % n_clusters_)
		# print('Estimated number of noise points: %d' % n_noise_)




		# X, labels_true = make_blobs(n_samples=750, centers=p1Vec, cluster_std=0.4,
  #                           random_state=0)
		# X = StandardScaler().fit_transform(p1Vec)
		
		# db = DBSCAN(eps=0.6, min_samples=10).fit(X)
		# core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
		# core_samples_mask[db.core_sample_indices_] = True
		# labels = db.labels_

		# # Number of clusters in labels, ignoring noise if present.
		# n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
		# n_noise_ = list(labels).count(-1)

		# print('Estimated number of clusters: %d' % n_clusters_)
		# print('Estimated number of noise points: %d' % n_noise_)
		


		# sorted_met = sorted(met, key = lambda k: k[2][0][0])
		# for m in sorted_met:
		# 	print(m)
		# for m in met:
		# 	print(m)
		return met

	def findVectorsOfWords(self, words):
		vec = []
		for word in words:
			vec.append(self.vectors[word])
		return vec

	def findCosineSimMatrix(self, p1Vec, p2Vec, p1Words, p2Words):
		lenP1 = len(p1Vec)
		lenP2 = len(p2Vec)
		lenWP1 = len(p1Words)
		lenWP2 = len(p2Words)
		met = [[0]*lenP2 for i in range(lenP1)]

		toSort = []
		for i in range(lenP1):
			for j in range(lenP2):
				# if not p1Vec[i].any() or not p2Vec[j].any():
				if not p1Vec[i] or not p2Vec[j]:
					met[i][j] = 1; continue
				
				cos = metrics.pairwise.cosine_similarity([array(p1Vec[i])],[array(p2Vec[j])])
				# print(p1Words[i], p2Words[j], cos[0][0])
				# cos[0][0] = 1 - cos[0][0]
				# met.append((p1Words[i], p2Words[j], cos))
				# met.append([cos])
				# met[i][j] = 1 - cos[0][0]
				# print(i,j,cos[0][0])
				if cos[0][0] > 1:
					cos[0][0] = 1
				met[i][j] = (math.acos(cos[0][0])/math.pi)
				toSort.append(met[i][j])
				# met[i][j] = cos[0][0]

		# sortedOne = sorted(toSort)
		# for k in sortedOne:
			# print(k)
		# for m in met:
		# 	print(m)
		return met

	def template_clustering(self, data, eps, minpts, amount_clusters = None, visualize = True, ccore = False):
	    # sample = read_sample(path_sample);
	    
	    optics_instance = optics(data, eps, minpts, amount_clusters, ccore);
	    (ticks, _) = timedcall(optics_instance.process);
	    
	    print("\t\tExecution time: ", ticks, "\n");

	    clusters = optics_instance.get_clusters();
	    noise = optics_instance.get_noise();
	    

	    print("clusters")
	    print(len(clusters), clusters)
	    print("noise")
	    print(len(noise),noise)

	    # if (visualize is True):
	    #     clusters = optics_instance.get_clusters();
	    #     noise = optics_instance.get_noise();
	    
	    #     visualizer = cluster_visualizer_multidim();	        
	    #     visualizer.append_clusters(clusters, data);
	    #     visualizer.append_cluster(noise, data, marker = 'x');
	    #     visualizer.show();
	    
	    #     ordering = optics_instance.get_ordering();
	    #     analyser = ordering_analyser(ordering);
	    #     # cluster_visualizer_multidim
	    #     ordering_visualizer.show_ordering_diagram(analyser, amount_clusters);

	# def clusterPapers(self, iVec, jVec):

















