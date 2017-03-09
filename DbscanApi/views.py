from django.shortcuts import render
from django.http import JsonResponse
import jieba
import numpy as np
import argparse,os,sys
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
import jieba
import gensim
from sklearn.metrics.pairwise import cosine_similarity
# Create your views here.
model = gensim.models.Word2Vec.load("Dbscapi/w2v_ch.model")
def dbsc(request):
	if request.POST and request.method =='POST':
		data = request.POST
		data = data.dict()
		e = float(data['e'])
		m = int(data['m'])
		doc = data['doc']
		eps=e
		minPts=m
		word=[]
		vector=[]
		number=['1','2','3','4','5','6','7','8','9','0']
		text=doc
		for n in number: #去掉數字
			text=text.replace(n,'')
		for x in jieba.cut(text): #斷詞
			if x!='\n' and x not in word:
				try:
					vector.append(model[x])
					word.append(x)
				except Exception as e:
					pass
		
		dist = 1 - cosine_similarity(vector) #cosine 距離矩陣計算
		db = DBSCAN(eps=eps,metric='precomputed', min_samples=minPts).fit(dist)#丟進function

		labels = db.labels_

		cluster={}
		for index,x in enumerate(word):
			if labels[index]!=-1:
				if str(labels[index]) not in cluster:
					cluster[str(labels[index])]=[x]
				else :
					cluster[str(labels[index])].append(x)
				#print x,labels[index]
		return JsonResponse(cluster, safe=False)
	return JsonResponse({'e':False,'m':False,'doc':False}, safe=False)
	