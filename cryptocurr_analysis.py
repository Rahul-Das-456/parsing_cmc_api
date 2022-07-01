import pandas as pd
import requests
from requests import Session
import pprint
import secret

#https://coinmarketcap.com/api/documentation/v1/ -> documentation

#test a basic request, url is header
#url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"


#headers = {
  #'Accepts': 'application/json',
  #'X-CMC_PRO_API_KEY': secret.api_key,
#}

#response = requests.get(url, headers=headers)

#print(response)

#print(response.status_code)

#data = response.json()

#pprint.pprint(data["data"][0])


class CMC:
    def __init__(self, token):
        self.apiurl = "https://pro-api.coinmarketcap.com"
        self.headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': token}
        self.session = Session()
        self.session.headers.update(self.headers)
    
    def get_all_coins(self):
        url = self.apiurl + "/v1/cryptocurrency/map"
        response = self.session.get(url)
        data = response.json()["data"]
        return data
    
    def get_price(self, symbol):
        url = self.apiurl + "/v1/cryptocurrency/quotes/latest"
        parameters = {"symbol": symbol}
        response = self.session.get(url, params = parameters) 
        data = response.json()["data"]
        return data

    
        
cmc = CMC(secret.api_key)

pprint.pprint(cmc.get_price("BTC"))