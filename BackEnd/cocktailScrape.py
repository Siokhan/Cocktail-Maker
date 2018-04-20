import requests
import json
import time

f = open('./Data/cocktailList.json', 'w+')

cocktail_list = []
for i in range(11000, 18000):

    if i % 100 == 0:
        print(i)

    try:
        res = requests.get("http://www.thecocktaildb.com/" + \
                "api/json/v1/1/lookup.php?i={}".format(i)).json()

        if res['drinks'] == None:
            continue

        drink = res['drinks'][0]

        ingredients = []
        for j in range(1, 16):
            ingredient = drink['strIngredient{}'.format(j)]
            if ingredient != None:
                ingredient = ingredient.strip()

            measure    = drink['strMeasure{}'.format(j)]
            if measure != None:
                measure = measure.strip() if measure != '' else None

            del drink['strIngredient{}'.format(j)]
            del drink['strMeasure{}'.format(j)]

            if ingredient == '':
                continue

            ingredients.append({
                'name': ingredient,
                'measure': measure
            })

        drink['ingredients'] = ingredients

        print("{} {}".format(i, drink['strDrink']))
        cocktail_list.append(drink)
    except Exception as e:
        print('Failed to download cocktail number {}: {}'.format( i, e))
        time.sleep(1)

f.write(json.dumps(cocktail_list, indent=4))

