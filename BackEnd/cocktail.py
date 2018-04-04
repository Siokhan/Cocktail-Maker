from random import shuffle
import json
import numpy as np 
import pandas as pd

cocktailKey = pd.read_csv('vectorKey.csv', encoding='ISO-8859-1')
num_Ingredients = len(cocktailKey.index)
print(num_Ingredients)

listOfIds = list(range(0,num_Ingredients))
shuffle(listOfIds)
for index in listOfIds[0:4]:
    print(cocktailKey.iloc[index]['ingredient'])
