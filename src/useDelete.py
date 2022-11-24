import requests
import json
bikeIdDelete = '637e731fb26f3e101c9b66a9'
def DataBeforeDelete():

  url = "https://data.mongodb-api.com/app/data-ipwwl/endpoint/data/v1/action/findOne"

  payload = json.dumps({
      "collection": "bikes",
      "database": "bikes",
      "dataSource": "Sandbox",
      "filter": {"_id":{"$oid" : bikeIdDelete}}
  })
  headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'qR8ioaiwVwnYxVUg75DzUT92yGkhQcSqbWr2xGO6dwVekV2hhbin8iP44XC0JQFW'
  }

  paramethers = {'clave1': 'valor1', 'clave2': 'valor2'}
  response = requests.request("POST", url, headers=headers, data=payload, params= paramethers)
  responseToText = response.text
  dict = json.loads(responseToText)
  consultationBefore = dict['document']
  return consultationBefore

def deleteOne():

  url = "https://data.mongodb-api.com/app/data-ipwwl/endpoint/data/v1/action/deleteOne"



  payload = json.dumps({
              "collection": "bikes",
              "database": "bikes",
              "dataSource": "Sandbox",
              "filter": {"_id":{"$oid" : bikeIdDelete}}
          })
  headers = {
          'Content-Type': 'application/json',
          'Access-Control-Request-Headers': '*',
          'api-key': 'qR8ioaiwVwnYxVUg75DzUT92yGkhQcSqbWr2xGO6dwVekV2hhbin8iP44XC0JQFW'
          }

  paramethers = {'clave1': 'valor1', 'clave2': 'valor2'}
  response = requests.request("POST", url, headers=headers, data=payload, params= paramethers)

def DataAfter():

  url = "https://data.mongodb-api.com/app/data-ipwwl/endpoint/data/v1/action/findOne"

  payload = json.dumps({
      "collection": "bikes",
      "database": "bikes",
      "dataSource": "Sandbox",
      "filter": {"_id":{"$oid" : bikeIdDelete}}
  })
  headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'qR8ioaiwVwnYxVUg75DzUT92yGkhQcSqbWr2xGO6dwVekV2hhbin8iP44XC0JQFW'
  }

  paramethers = {'clave1': 'valor1', 'clave2': 'valor2'}
  response = requests.request("POST", url, headers=headers, data=payload, params= paramethers)
  hola = response.text
  dict = json.loads(hola)
  consultationAfter = dict['document']
  return consultationAfter

# def checkDelete(consultaAntes, consultaDespues):
#   if consultaAntes == consultaDespues:
#     print ('No se ha podido borrar')
#   else:
#     print('Borrado correctamente')
  




dataBefore = DataBeforeDelete()
deleteOne()
ActualData  = DataAfter()

if  dataBefore == ActualData:
  print ('No se ha podido borrar')
else:
  print('Borrado correctamente')


