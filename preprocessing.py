import os
import json
import gzip
import pandas as pd
from urllib.request import urlopen
from datetime import datetime
import random
import numpy as np
from tqdm import notebook as tqdm
from collections import defaultdict
from datetime import datetime
import pickle
from sentence_transformers import SentenceTransformer

def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

reviews = defaultdict(list)
missing=0
with gzip.open("reviews_Kindle_Store_5.json.gz", 'r') as f:
    for l in f:
        r = json.loads(l.strip())
        #r['reviewTime'] = datetime.strptime(r['reviewTime'], '%m %d, %Y').date()
        #a = r['reviewerID']
        #reviews[a].append(r)
        
        a = r['reviewerID']
        try:
            reviews[a].append({r['asin']:r['reviewText']})
        except:
            missing +=1
            reviews[a].append({r['asin']:' '})
#for k,values in reviews.items():
    #reviews[k] = sorted(values, key=lambda x: x['reviewTime'])
    #reviews[a] = sorted(reviews[a], key=lambda x: x['reviewTime'])
user_list = []
items_list = []
for k,values in reviews.items():
    if len(values) > 18:
        user_list.append(k)
        items_list.append([x['asin'] for x in values])
        
all_items = []
for i in items_list:
    all_items.extend(i)
all_items = set(all_items)
len(all_items)

user_dict = {}
items_dict = {}
count = 0
for i in user_list:
    user_dict[i] = count
    count += 1
count = 0
for i in all_items:
    items_dict[i] = count
    count += 1

sbert_model =  SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2',device='cuda:1')
reviews_vec=[]
for i in user_reviews:
    if len(i) >= 2:
        reviews_vec.append(sbert_model.encode(i))
first_haft=[]
second_haft=[]
for i in reviews_vec:
    n = len(i)
    first_haft.append(np.mean(i[:n//2],axis=0))
    second_haft.append(np.mean(i[n//2:],axis=0))

pos_res=[]
neg_res=[]
for i in range(len(first_haft)):
    a = cosine(first_haft[i], second_haft[i])
    b = cosine(first_haft[i], second_haft[random.randint(0,len(first_haft)-1)])
    
    pos_res.append(a)
    neg_res.append(b)
with open('kindleReviewVec.pkl', 'wb') as f:
    pickle.dump(reviews_vec, f)