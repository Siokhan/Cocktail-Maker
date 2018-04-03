import json
import pandas as pd 
import numpy as np 
from pandas import DataFrame

masterList = []

with open('input.json') as json_data:
    d = json.load(json_data)
    for ingredient in d['drinks']:
        masterList.append(ingredient['strIngredient1'])
    #print(masterList)

file = open('vectorKey.csv', 'w+')
file.write('ingredient, vector\n')
for index, i in enumerate(masterList):
    print(i, index, end='\n')
    file.write('{}, {}\n'.format(i, index))
