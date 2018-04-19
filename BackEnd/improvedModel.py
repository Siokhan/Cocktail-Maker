from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import SGDClassifier
from sklearn import svm
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

data = pd.read_csv('popularity.csv', encoding='ISO-8859-1')
feature = ['ingredientsHashed']
totalEntries = len(data.index)
print(totalEntries)
X = data.loc[:, feature]
y = data.adjustedrating
hashlist = []

for i in range(0, totalEntries):
    hashes = data.get_value(i, 'ingredientsHashed')
    hashlist.append(hashes)
X3 = biVectorizer.fit_transform(hashlist)
## classifier ##

clf = SGDClassifier(loss='hinge', penalty='l2', max_iter=5, shuffle=False)
clf.fit(X3, y)

test = ['11bc496ff310d1aae4df6ff0e8ff968a fc1cebf02dc2ee68655f3e7bf1b84230 9d3bce8eb5cec78e54d36dd0daf2bdc5 7d73dc0b6f7aeb20d99293fbdc5d6a6f 5ac0adcafdfad50d321f7cbcbe0060a0']
badtest = ['3f3e574c181f45eea2aa2548e75f4434 909cea0c97058cfe2e3ea8d675cb08e1 99ba0855ce410fd0b68e2ceda2ffe98f e8f504860d2fbf92d26e69c85bc1486a 80766a792c83776a1302211303533d76']
xtest = biVectorizer.transform(test)
ytest = biVectorizer.transform(badtest)
predicted = clf.predict(xtest)
badpredicted = clf.predict(ytest)
print(predicted)
print(badpredicted)