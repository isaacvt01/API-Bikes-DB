import requests
import json
url = "https://data.mongodb-api.com/app/data-ipwwl/endpoint/data/v1/action/aggregate"

payload = json.dumps({
    "collection": "bikes",
    "database": "bikes",
    "dataSource": "Sandbox",
    "pipeline": [
        {
          "$lookup": {
            "from": "tiendas",
            "localField": "tiendaID",
            "foreignField": "tiendaID",
            "as": "Belongs to the shop: "
          }
        }
      ]
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'qR8ioaiwVwnYxVUg75DzUT92yGkhQcSqbWr2xGO6dwVekV2hhbin8iP44XC0JQFW'
}

parameters = {'clave1': 'valor1', 'clave2': 'valor2'}
response = requests.request("POST", url, headers=headers, data=payload, params= parameters)
cont = 0
responseToText = response.text
dict = json.loads(responseToText)
consultation = dict['documents']
for item in consultation:
    print (str(item) + '\n')
    cont = cont + 1