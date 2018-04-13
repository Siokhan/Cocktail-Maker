import json

masterList = []

with open('input.json') as json_data:
    d = json.load(json_data)
    for ingredient in d['drinks']:
        masterList.append(ingredient['strIngredient1'])

file = open('vectorKey.json', 'w+')
cocks = []
for index, name in enumerate(masterList):
    print(name, index, end='\n')
    cocks.append({
        "index": index,
        "name": name
    })
    # file.write('{}, {}\n'.format(i, index))
json.dump(cocks, file)