from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
import json
import numpy as np
import pandas as pd
import csv

cocktailList = []
corpus = []
vectorizer = CountVectorizer()
biVectorizer = CountVectorizer(ngram_range=(1, 2), token_pattern=r'\b\w+\b', min_df=1)

with open('cocktailsVector.txt') as openfile:
    for line in openfile:
        x = line.split(' ')
        #print(vectorizer.fit_transform(x))
        #print(line)
        cocktailList.append({
            'ingredients': line,
            'label': 'valid'
        })
        corpus.append(line)

json.dump(cocktailList, open('labels.json', 'w+'))   
            
X2 = biVectorizer.fit_transform(corpus)
shape = X2.shape
#print(X2)
#print(corpus)
#print(shape)

data = pd.read_csv('cocktails.csv', encoding='ISO-8859-1')
feature = ['ingredients']
X = data.loc[:, feature]
y = data.label
print(y.shape)
print(X)

## classifier ##

clf = svm.SVC()
clf.fit(X2, y)

gnb = GaussianNB()
gnb.fit(X2.toarray(), y)

test = ['11bc496ff310d1aae4df6ff0e8ff968a fc1cebf02dc2ee68655f3e7bf1b84230 9d3bce8eb5cec78e54d36dd0daf2bdc5 7d73dc0b6f7aeb20d99293fbdc5d6a6f 5ac0adcafdfad50d321f7cbcbe0060a0']
badtest = ['0950210a45488b218b5ec9387827b69c 0950210a45488b218b5ec9387827b69c 0950210a45488b218b5ec9387827b69c 0950210a45488b218b5ec9387827b69c 0950210a45488b218b5ec9387827b69c 0950210a45488b218b5ec9387827b69c 0950210a45488b218b5ec9387827b69c 0950210a45488b218b5ec9387827b69c 0950210a45488b218b5ec9387827b69c']
xtest = biVectorizer.transform(test)
predicted = clf.predict(xtest)
predicted2 = gnb.predict(test)
print(predicted)
print(predicted2)