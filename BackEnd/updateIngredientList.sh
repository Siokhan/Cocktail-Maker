rm input.json
curl https://www.thecocktaildb.com/api/json/v1/1/list.php?i=list >> input.json
python3 organizeIngredients.py 