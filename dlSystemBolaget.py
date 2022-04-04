from itertools import product
import requests
import json
import os

OcpApimSubscriptionKeyFile = open("OcpApimSubscriptionKey.txt", "r")
OcpApimSubscriptionKey = OcpApimSubscriptionKeyFile.read()
OcpApimSubscriptionKeyFile.close()

baseURLSearch = "https://api-extern.systembolaget.se/sb-api-ecommerce/v1/productsearch/search"
storeId = "1442" # default Oslovägen 56
additionalParameters = "&sortBy=Price&sortDirection=Ascending&size=30&isInDepotStockForFastDelivery=0&isInStoreAssortmentSearch=true"
dataPath = '.\\data\\'

if not os.path.exists(dataPath):
    os.makedirs(dataPath)

pageNum = 1

while True:
	response = requests.get(f"{baseURLSearch}?page={pageNum}&storeId={storeId}{additionalParameters}",stream = True, headers={'Ocp-Apim-Subscription-Key':OcpApimSubscriptionKey})
	if response.status_code != 200:
		break
	obj = json.loads(response.text)
	products = obj["products"]
	if len(products) <= 0:
		break
	f = open(f"{dataPath}page{pageNum}.json", "w")
	f.write(response.text)
	f.close()
	print(f"Downloaded page {pageNum}")
	pageNum += 1

