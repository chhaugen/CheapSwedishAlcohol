import json

dataPath = '.\\data\\'

f = open(f"{dataPath}products.json", "r")
obj = json.loads(f.read())
f.close()

cleanProducts = {}
for i in obj:
    prodId = int(i["productId"])
    alcoholPercentage = i["alcoholPercentage"]
    prodName = f"{i['productNameBold']} {i['productNameThin']}"
    if prodId in cleanProducts:
        print(f"Duplicate: {prodId}: {prodName}")
    if alcoholPercentage <= 0:
        print(f"NonAlcoSkip: {prodId}: {prodName}")
        continue
    cleanProducts[prodId] = i

f = open(f"{dataPath}productsClean.json", "w")
f.write(json.dumps(list(cleanProducts.values())))
f.close()