from flask import Flask, request
application = Flask(__name__)

in_memory_datastore = {
   "COBOL": {"name": "COBOL", "publication_year": 1960, "contribution": "record data"},
   "ALGOL": {"name": "ALGOL", "publication_year": 1958, "contribution": "scoping and nested functions"},
   "APL": {"name": "APL", "publication_year": 1962, "contribution": "array processing"},
   "BASIC": {"name": "BASIC", "publication_year": 1964, "contribution": "runtime interpretation, office tooling"},
   "PL": {"name": "PL", "publication_year": 1966, "contribution": "constants, function overloading, pointers"},
   "SIMULA67": {"name": "SIMULA67", "publication_year": 1967,
                "contribution": "class/object split, subclassing, protected attributes"},
   "Pascal": {"name": "Pascal", "publication_year": 1970,
              "contribution": "modern unary, binary, and assignment operator syntax expectations"},
   "CLU": {"name": "CLU", "publication_year": 1975,
           "contribution": "iterators, abstract data types, generics, checked exceptions"},
}

@application.route('/')
def hello_world():
    return "Fuck off"
@application.route('/programming_languages/<programming_language_name>')
def get_programming_language(programming_language_name):
   return in_memory_datastore[programming_language_name]

import requests 
import base64
user='clevercart-c4a68e29f9afcc45f2e56902f0151c991072864823612119086'
passw = '25MY35fFo7Uh7fZJfzdrB17OJ42VC4rnFTd4jhI4'
code_it = user+':'+passw
message_bytes = code_it.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')
code_it = "Basic "+base64_message

def get_me_the_fuck_in():
    headers = {"Content-Type":"application/x-www-form-urlencoded","Authorization":code_it}
    data = {"grant_type":"client_credentials","scope":"product.compact"}
    
    resp = requests.post('https://api.kroger.com/v1/connect/oauth2/token', headers=headers,data = data)
    
    response_data = resp.json()
    return response_data['access_token']
def get_me_the_fuck_locations(access_token):
    header_locations = {"Accept": "application/json","Authorization": "Bearer "+access_token}
    res = requests.get('https://api.kroger.com/v1/locations?filter.zipCode.near=47408&filter.radiusInMiles=15&filter.chain=Kroger',headers=header_locations)
    chain_loc = res.json()

    ids = []
    for i in chain_loc["data"]:
        ids.append(i['locationId'])
    return ids

def get_me_the_fuck_cheap(locations,access_token,term,brand):
    res = ''
    for id in locations:
        header_cheap = {"Accept": "application/json","Authorization": "Bearer "+access_token}
        get_me_the_url="https://api.kroger.com/v1/products?filter.brand="+brand+"&filter.term="+term+"&filter.locationId="+str(id)
        res = requests.get(get_me_the_url,headers=header_cheap)

    data = res.json()
    return data["data"][0]["productId"]

def fuckin_cheap_value(prod,access_token,location):

    header_cheap = {"Accept": "application/json","Authorization": "Bearer "+access_token}
    get_me_the_url="https://api.kroger.com/v1/products/"+str(prod)+"?filter.locationId="+str(location)

    res = requests.get(get_me_the_url,headers=header_cheap)

    data = res.json()

    return data["data"]["items"][0]["price"]

access_token=get_me_the_fuck_in()
locs = get_me_the_fuck_locations(access_token)

productid = get_me_the_fuck_cheap(locs,access_token,'chocolate','Kroger')


@application.get('/kroger/<item>')
def list_of_items(item):
   productid = get_me_the_fuck_cheap(locs,access_token,item,'Kroger')
   return_value = fuckin_cheap_value(productid,access_token,locs[0])
   return {"programming_languages":list(return_value.values())}


