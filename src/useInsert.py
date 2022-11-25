import requests
import json
url = "https://data.mongodb-api.com/app/data-ipwwl/endpoint/data/v1/action/insertOne"

brandValue = 'MegaSuperBikes'
frameValue = 44 
typeValue = 'Black'
tiendaID = 3

payload = json.dumps({
    "collection": "bikes",
    "database": "bikes",
    "dataSource": "Sandbox",
    "document": {
        "brand": brandValue,
        "frame": frameValue,
        'bike_type': typeValue,
        "tiendaID": tiendaID
      }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'qR8ioaiwVwnYxVUg75DzUT92yGkhQcSqbWr2xGO6dwVekV2hhbin8iP44XC0JQFW'
}

parameters = {'clave1': 'valor1', 'clave2': 'valor2'}
response = requests.request("POST", url, headers=headers, data=payload, params= parameters)




