import requests
import json
url = "https://data.mongodb-api.com/app/data-ipwwl/endpoint/data/v1/action/aggregate"

payload = json.dumps({
    "collection": "bikes",
    "database": "bikes",
    "dataSource": "Sandbox",
    "pipeline": [
        {
          "$group": {
            "_id": "$brand",
            "count": { "$sum": 1 },
          }
        },
        { "$sort": { "count": 1 } }
      ]
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'qR8ioaiwVwnYxVUg75DzUT92yGkhQcSqbWr2xGO6dwVekV2hhbin8iP44XC0JQFW'
}

parametros = {'clave1': 'valor1', 'clave2': 'valor2'}
response = requests.request("POST", url, headers=headers, data=payload, params= parametros)
contador = 0
hola = response.text
diccionario = json.loads(hola)
consulta = diccionario['documents']
for item in consulta:
    print (item)
    contador = contador + 1