# -*- coding:utf-8 -*-

import sys
import re
import numpy as np
from sklearn.externals import joblib
import csv
import matplotlib.pyplot as plt
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import cross_validate 
import os
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE

#minimum lenght of a dns name
MIN_LEN=10

#random state
random_state = 170
#random_state = 1


def load_alexa(filename):
    domain_list=[]
    csv_reader = csv.reader(open(filename))
    for row in csv_reader:
        domain=row[1]
        #print(domain)
        if len(domain) >= MIN_LEN:
            domain_list.append(domain)
    return domain_list

def domain2ver(domain):
    ver=[]
    for i in range(0,len(domain)):
        ver.append([ord(domain[i])])
    return ver


def load_dga(filename):
    domain_list=[]
    #xsxqeadsbgvpdke.co.uk,Domain used by Cryptolocker - Flashback DGA for 13 Apr 2017,2017-04-13,
    # http://osint.bambenekconsulting.com/manual/cl.txt
    with open(filename) as f:
        for line in f:
            domain=line.split(",")[0]
            if len(domain) >= MIN_LEN:
                domain_list.append(domain)
    return  domain_list


#load dns data
x1_domain_list = load_alexa("./dga/top-100.csv")
x2_domain_list = load_dga("./dga/dga-cryptolocke-50.txt")
x3_domain_list = load_dga("./dga/dga-post-tovar-goz-50.txt")

x_domain_list=np.concatenate((x1_domain_list, x2_domain_list,x3_domain_list))


y1=[0]*len(x1_domain_list)
y2=[1]*len(x2_domain_list)
y3=[1]*len(x3_domain_list)

y=np.concatenate((y1, y2,y3))

#print (x_domain_list)

cv = CountVectorizer(ngram_range=(2, 2), decode_error="ignore",
                                      token_pattern=r"\w", min_df=1)
x= cv.fit_transform(x_domain_list).toarray()

# apply KMeans and TSNE ...










