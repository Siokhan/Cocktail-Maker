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
    file.write('{}, {}\n'.format(i, index))
