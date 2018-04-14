import json
import hashlib

masterList = []
cocktailList = []

with open('cocktailList.json') as json_data:
    d = json.load(json_data)
    for cocktail in d:
        cocktailList.append(cocktail['ingredients'])

def hash(str):
    return hashlib.md5(str.encode()).hexdigest()

setName = set()
for i, cocktail in enumerate(cocktailList):
    for ingredient in cocktail:
        if(ingredient['name'] != None):
            setName.add(ingredient['name'])

for i in range(0, len(setName)):
    name = setName.pop()
    masterList.append({
        'name': name,
        'hash': hash(name)
    })

numIngredients = len(masterList)
print(masterList)
print(numIngredients)
file = open('vectorKey.json', 'w+')
json.dump(masterList, file)