from itertools import islice
import json
from unicodedata import category
from prettytable import PrettyTable
import os

dataPath = '.\\data\\'
resultsPath = '.\\results\\'
if not os.path.exists(resultsPath):
    os.makedirs(resultsPath)

def prettyTableOfProducts(products):
    headers = ["Name", "ml alcohol per 100SEK", "Volume ml", "% Alcohol", "Kr", "Category"]
    table = PrettyTable(headers)
    table.float_format = '.2'
    for product in products:
        prodName = ""
        if product['productNameThin'] == None:
            prodName = f"{product['productNameBold']}"
        else:
            prodName = f"{product['productNameBold']} {product['productNameThin']}"
        kr = product["price"]
        alcoholPercentage = product["alcoholPercentage"]
        volume = product["volume"]
        category = f"{product['categoryLevel1']}, {product['categoryLevel2']}"
        mlAlcoholPer100kr = product["mlAlcoholPer100Kr"]
        table.add_row([
            prodName, mlAlcoholPer100kr, volume, alcoholPercentage, kr, category
        ])
    return table

def mlAlcoholPer100Kr(kr, volume, alcoholPerc):
    alcoholVolume_ml = volume * alcoholPerc / 100
    return alcoholVolume_ml * 100 / kr

f = open(f"{dataPath}productsClean.json", "r")
products = json.loads(f.read())
f.close()

for product in products:
    kr = product["price"]
    alcoholPercentage = product["alcoholPercentage"]
    volume = product["volume"]

    product["mlAlcoholPer100Kr"] = mlAlcoholPer100Kr(kr, volume, alcoholPercentage)

products = sorted(products, key=lambda x: x["mlAlcoholPer100Kr"], reverse=True)


# productsSorted = list(islice(productsSorted, 200))

f = open(f"{resultsPath}LeastKrPerAlcoholml.json", "w")
f.write(json.dumps(products))
f.close()


productsAboveTwenty = list(filter(lambda x: x["alcoholPercentage"] > 20, products))
productsAboveTwenty = sorted(productsAboveTwenty, key=lambda x: x["mlAlcoholPer100Kr"], reverse=True)

f = open(f"{resultsPath}LeastKrPerAlcoholml_MinimumAlcohol20Perc.json", "w")
f.write(json.dumps(productsAboveTwenty))
f.close()
        

f = open(f"{resultsPath}LeastKrPerAlcoholmlTable.html", "w")
f.write(prettyTableOfProducts(products).get_html_string(format=True))
f.close()


f = open(f"{resultsPath}LeastKrPerAlcoholmlTable_MinimumAlcohol20Perc.html", "w")
f.write(prettyTableOfProducts(productsAboveTwenty).get_html_string(format=True))
f.close()