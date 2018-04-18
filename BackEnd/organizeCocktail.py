import json
import numpy as np
import pandas as pd
from pandas import DataFrame
import csv
import math

cocktailList = []
ingredientList = []

def vectorizer(name):
    for item in ingredientList:
        if item['name'] == name:
            return item['hash']
    return None

def adjuster(oldValue):
    populardf = pd.read_csv('popularity.csv', encoding='ISO-8859-1')
    oldMax = populardf['rating'].max()
    oldMin = populardf['rating'].min()
    newMax = 10
    newMin = 0
    oldRange = (oldMax - oldMin)
    newRange = (newMax - newMin)
    newValue = (((oldValue - oldMin) * newRange) / oldRange) + newMin
    return newValue

def transform(popularVal):
    transformed = np.log10(popularVal)
    return transformed

with open('cocktailList.json') as json_data:
    d = json.load(json_data)
    for cocktail in d:
        cocktailList.append(cocktail['ingredients'])

with open('vectorKey.json') as json_data:
    ingredientList = json.load(json_data)

file2 = open('cocktails.txt', 'w+')
for i, cocktail in enumerate(cocktailList):
    for ingredient in cocktail:
        if(ingredient['name'] != None):
            #print('gucci', ingredient['name'])
            file2.write(ingredient['name'] + ' ')
    file2.write('\n')

## adjusting popularity value to be more readable ##
popularitydf = pd.read_csv('popularity.csv', encoding='ISO-8859-1', index_col=0)
popularitydf['rating'] = '0'
popularitydf['adjustedrating'] = '0'
popularitydf['ingredients(hashed)'] = 'abc'
maxIndex = len(popularitydf.index)
for i in range(0, maxIndex):
    popVal = popularitydf.get_value(i, 'popularity')
    newPop = transform(popVal)
    popularitydf.set_value(i, 'rating', value=newPop)
    rating = popularitydf.get_value(i, 'rating')
    newRating = adjuster(rating)
    popularitydf.set_value(i, 'adjustedrating', value=newRating)
popularitydf.to_csv('popularity.csv')

## Creating CSV file with cocktails and their attributes ##
cocktailsParsed = json.load(open('labels.json'))
cockData = open('cocktails.csv', 'w+')

csvwriter = csv.writer(cockData)

count = 0
for cock in cocktailsParsed:
    if count == 0:
        header = cock.keys()
        csvwriter.writerow(header)
        count += 1
    csvwriter.writerow(cock.values())
cockData.close()

## Adding hashed ingredients to popularity table ##
ingredientdf = pd.read_csv('cocktails.csv', encoding='ISO-8859-1')
for i in range(0, maxIndex):
    cockIngredients = ingredientdf.get_value(i, 'ingredients')
    popularitydf.set_value(i, 'ingredients(hashed)', value=cockIngredients)
popularitydf.to_csv('popularity.csv')
