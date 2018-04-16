from sklearn.feature_extraction.text import CountVectorizer
import json
import numpy as np

cocktailList = []
corpus = []
vectorizer = CountVectorizer()
biVectorizer = CountVectorizer(ngram_range=(1, 2), token_pattern=r'\b\w+\b', min_df=1)

# with open('cocktailList.json') as json_data:
#     d = json.load(json_data)
#     for cocktail in d:
#         cocktailList.append(cocktail['ingredients'])

with open('cocktailsVector.txt') as openfile:
    for line in openfile:
        x = line.split(' ')
        print(vectorizer.fit_transform(x))
        print(line)
        cocktailList.append({
            "ingredients": line,
            "label": 'valid'
        })
        corpus.append(line)

json.dump(cocktailList, open('labels.json', 'w+'))   
            
X2 = biVectorizer.fit_transform(corpus)
shape = X2.shape
print(X2)
#print(corpus)
#print(shape)