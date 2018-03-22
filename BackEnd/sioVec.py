import pandas as pd
import numpy as np
import re
import json
import requests

page = requests.get("https://www.thecocktaildb.com/api/json/v1/1/list.php?i=list")

