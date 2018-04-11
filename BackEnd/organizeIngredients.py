import json

masterList = []

with open('input.json') as json_data:
    d = json.load(json_data)
    for ingredient in d['drinks']:
        masterList.append(ingredient['strIngredient1'])

file = open('vectorKey.csv', 'w+')
file.write('ingredient, vector\n')
for index, i in enumerate(masterList):
    print(i, index, end='\n')
    file.write('{}, {}\n'.format(i, index))
