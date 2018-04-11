import json

cocktailList = []

with open('cocktailList.json') as json_data:
    d = json.load(json_data)
    for cocktail in d:
        cocktailList.append(cocktail['ingredients'])

file = open('cocktailKey.csv', 'w+')
file.write('cocktail, vector\n')
for index, i in enumerate(cocktailList):
    print(i, index, end='\n')
    for ingredient in i:
        if(ingredient['name'] != None):
            file.write('{}, '.format(ingredient['name']))
    file.write('\n')
