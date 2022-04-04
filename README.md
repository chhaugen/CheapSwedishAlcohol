# CheapSwedishAlcohol

## Requrements:
- Python 3.7
- requests
- prettytable

## How to get OcpApimSubscriptionKey from systembolaget.se (using Firefox):
- Do a search on systembolaget.no
- Open Inspect (F12)
- Go to the Network tab
- Reload the site.
- Sort by Type
- Find json files
- Find the one from https://api-extern.systembolaget.se/sb-api-ecommerce/v1/productsearch/search
- Click on it
- Scroll down to Request Headers
- Copy the string after "Ocp-Apim-Subscription-Key: " into OcpApimSubscriptionKey.txt

## Running
Run the scripts in this order:
- dlSystemBolaget.py
- parseSystemBolaget.py
- cleanProductsJson.py
- analyseCleanProductsJson.py

## Notes:

https://api-extern.systembolaget.se/sb-api-ecommerce/v1/productsearch/search
has a max page count off 334. This might indicate that data may be out of reach 