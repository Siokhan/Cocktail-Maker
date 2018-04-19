from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import SGDClassifier
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
        #print(vectorizer.fit_transform(x))
        #print(line)
        cocktailList.append({
            'ingredients': line,
            'label': 'valid'
        })
        corpus.append(line)

json.dump(cocktailList, open('labels.json', 'w+'))   

## Machine learning begin below ##            
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
joblib.dump(clf, 'classifier.pkl')

test = ['916a17d53dff7bbd06635fac294e86eb e89b2cbb7d11825a67459af2249064de']
badtest = ['3f3e574c181f45eea2aa2548e75f4434 909cea0c97058cfe2e3ea8d675cb08e1 99ba0855ce410fd0b68e2ceda2ffe98f e8f504860d2fbf92d26e69c85bc1486a 80766a792c83776a1302211303533d76']
xtest = biVectorizer.transform(test)
ytest = biVectorizer.transform(badtest)
predicted = clf.predict(xtest)
badpredicted = clf.predict(ytest)
print(predicted)
print(badpredicted)