from sklearn.feature_extraction.text import CountVectorizer
import json

cocktailList = []
corpus = []
vectorizer = CountVectorizer()
biVectorizer = CountVectorizer(ngram_range=(1, 2), token_pattern=r'\b\w+\b', min_df=1)

with open('cocktailList.json') as json_data:
    d = json.load(json_data)
    for cocktail in d:
        cocktailList.append(cocktail['ingredients'])

with open('cocktails.txt') as openfile:
    for line in openfile:
        x = [line]
        print(biVectorizer.fit_transform(x))
        print(line)
        corpus.append(line)
            
X2 = biVectorizer.fit_transform(corpus)
print(X2)
print(corpus)