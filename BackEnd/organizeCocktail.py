import json

cocktailList = []
ingredientList = []

def vectorizer(name):
    for item in ingredientList:
        if item['name'] == name:
            return item['hash']
    return None

with open('cocktailList.json') as json_data:
    d = json.load(json_data)
    for cocktail in d:
        cocktailList.append(cocktail['ingredients'])

with open('vectorKey.json') as json_data:
    ingredientList = json.load(json_data)

file = open('cocktailsVector.txt', 'w+')
cocktailsVector = []
for i, cocktail in enumerate(cocktailList):
    for ingredient in cocktail:
        if(ingredient['name'] != None):
            print('gucci', ingredient['name'])
            file.write(str(vectorizer(ingredient['name'])) + ' ')
    file.write('\n')
