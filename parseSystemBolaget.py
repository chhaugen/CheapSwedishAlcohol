import json
import glob

dataPath = '.\\data\\'

def getProductsFromPage(filePath):
    f = open(filePath, "r")
    obj = json.loads(f.read())
    f.close()
    productsList = []
    objProduncts = obj["products"]
    for x in obj["products"]:
        productsList.append(x)
    return productsList

products = []

fileNames = glob.glob(f'{dataPath}page*.json')

for fileName in fileNames:
  products += getProductsFromPage(fileName)

f = open(f"{dataPath}products.json", "w")
f.write(json.dumps(products))
f.close()