import requests
import json

fieldValue = 'Bicicletas'
updateValue = 'Biciclesssstas'

url = "https://data.mongodb-api.com/app/data-ipwwl/endpoint/data/v1/action/updateMany"

payload = json.dumps({
    "collection": "bikes",
    "database": "bikes",
    "dataSource": "Sandbox",
    "filter": {"brand":fieldValue},
    "update":{
        "$set": {
            "brand": updateValue
        }
    }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'qR8ioaiwVwnYxVUg75DzUT92yGkhQcSqbWr2xGO6dwVekV2hhbin8iP44XC0JQFW'
}


response = requests.request("POST", url, headers=headers, data=payload)
