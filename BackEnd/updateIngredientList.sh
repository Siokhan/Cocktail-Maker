rm input.json
curl https://www.thecocktaildb.com/api/json/v1/1/list.php?i=list >> input.json
rm ingredientList.json
python3 organize.py >> ingredientList.json