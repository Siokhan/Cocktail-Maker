from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.externals import joblib
import json
import numpy as np
import pandas as pd
import csv
import pickle

cocktailList = []
corpus = []
vectorizer = CountVectorizer()
biVectorizer = CountVectorizer(ngram_range=(1, 2), token_pattern=r'\b\w+\b', min_df=1)

with open('cocktailsVector.txt') as openfile:
    for line in openfile:
        x = line.split(' ')
        cocktailList.append({
            'ingredients': line,
            'label': 'valid'
        })
        corpus.append(line)

json.dump(cocktailList, open('labels.json', 'w+'))   

## Data for classifier organized ##            
data = pd.read_csv('popularity.csv', encoding='ISO-8859-1')
feature = 'ingredientsHashed'
totalEntries = len(data.index)
print(totalEntries)
hashlist = []
for i in range(0, totalEntries):
    hashes = data.get_value(i, feature)
    hashlist.append(hashes)
X = biVectorizer.fit_transform(hashlist)
y = data.adjustedrating

## classifier ##
clf = SGDClassifier(loss='hinge', penalty='l2', max_iter=5, shuffle=False)
clf.fit(X, y)
joblib.dump(clf, 'SGDclassifier.pkl')

clf2 = svm.SVC()
clf2.fit(X, y)

gnb = GaussianNB()
gnb.fit(X.toarray(), y) 

test = ['916a17d53dff7bbd06635fac294e86eb 4ca90a18e9f0d1242171c3c66074714b']
badtest = ['3f3e574c181f45eea2aa2548e75f4434 909cea0c97058cfe2e3ea8d675cb08e1 80766a792c83776a1302211303533d76']
xtest = biVectorizer.transform(test)
ytest = biVectorizer.transform(badtest)
clfPredicted = clf.predict(xtest)
clfBadpredicted = clf.predict(ytest)

clf2Predicted = clf2.predict(xtest)
clf2Badpredicted = clf2.predict(ytest)

gnbPredicted = gnb.predict(xtest.toarray())
gnbBadpredicted = gnb.predict(ytest.toarray())

print(clfPredicted)
print(clfBadpredicted)

print(clf2Predicted)
print(clf2Badpredicted)

print(gnbPredicted)
print(gnbBadpredicted)