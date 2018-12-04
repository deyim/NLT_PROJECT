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

class DimensionRelatedness:

	def __init__(self, VECTORFILE, OUTFILE, DIR, FILENUM, THRESHOLD):
		self.vectors = self.getVectors(VECTORFILE)
		self.outfile = OUTFILE
		self.DIR = DIR
		self.FILENUM = FILENUM
		self.Threshold = THRESHOLD
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

	def filterWords(self, words):
		newWords = []
		for word in words:
			if word not in self.vectors:
				continue
			newWords.append(word)
		return newWords 

	def findVectorsOfWords(self, words):
		vec = []
		for word in words:
			vec.append(self.vectors[word])
		return vec

	def findRelatedness(self):
		# test set
		# self.pairRelatedness(1,2)
		relMat = [[0]*self.FILENUM for i in range(self.FILENUM)]

		f = open(self.outfile, "w")

		for i in range(1,self.FILENUM):
			for j in range(1,self.FILENUM):
				# if i==j: continue
				rel, relNorm = self.pairRelatedness(i,j)
				print(i,j,rel,relNorm)
				relMat[i][j] = rel
				# ary.append((i,j,rel))
				# print(i,j,rel)
				f.write(str(i) +'\t'+ str(j) +'\t' + str(relNorm) +'\n')

		# for met in relMat:
		# 	print(met)

		f.close()

	def pairRelatedness(self, i, j):
		P1 = open(self.DIR+str(i)+".txt")
		P2 = open(self.DIR+str(j)+".txt")
		p1Words = self.filterWords(P1.readline().split())
		p2Words = self.filterWords(P2.readline().split())
		P1.close(); P2.close()
		p1Vec = self.findVectorsOfWords(p1Words) 
		p2Vec = self.findVectorsOfWords(p2Words)


		met = self.findCosineSimMatrix(p1Vec, p2Vec, p1Words, p2Words)
		
		rel = 0; cnt = 0
		for i in range(len(met)):
			for j in range(len(met[0])):
				if met[i][j] >= self.Threshold:
					rel += met[i][j]
					cnt += 1

		normDenom = (len(p1Words)/25) * (len(p2Words)/25)
		denom = cnt / normDenom
		return rel, rel / denom

	def findCosineSimMatrix(self, p1Vec, p2Vec, p1Words, p2Words):
		lenP1 = len(p1Vec)
		lenP2 = len(p2Vec)
		lenWP1 = len(p1Words)
		lenWP2 = len(p2Words)
		met = [[0]*lenP2 for i in range(lenP1)]

		for i in range(lenP1):
			for j in range(lenP2):
				# if not p1Vec[i].any() or not p2Vec[j].any():
				if not p1Vec[i] or not p2Vec[j]:
					met[i][j] = 1; continue
				
				cos = metrics.pairwise.cosine_similarity([array(p1Vec[i])],[array(p2Vec[j])])
				met[i][j] = cos[0][0]

		return met




