import json
import requests

masterList = []

with open("input.json") as json_data:
    d = json.load(json_data)
    # print(d['drinks'])
    for ingredient in d['drinks']:
        masterList.append(ingredient['strIngredient1'])
    print(masterList)