from random import shuffle
import json
import numpy as np 
import pandas as pd

ingredientKey = pd.read_csv('vectorKey.csv', encoding='ISO-8859-1')
num_Ingredients = len(ingredientKey.index)
print(num_Ingredients)

listOfIds = list(range(0,num_Ingredients))
shuffle(listOfIds)
for index in listOfIds[0:4]:
    print(ingredientKey.iloc[index]['ingredient'])
