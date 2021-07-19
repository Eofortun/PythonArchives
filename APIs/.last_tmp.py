import requests
import json
    
Url = "http://economia.awesomeapi.com.br/json/all/"
    
def Dolar():
    D = requests.get(Url+"USD")
    Text = D.text
    Valor = json.loads(Text)    
    Dolar = Valor.get("USD").get("high")
    
    return Dolar

def Euro():
    E = requests.get(Url+"EUR")
    Text = E.text
    Valor = json.loads(Text)
    Euro = Valor.get("EUR").get("high")    
    
    return Euro

def LibraEsterlina():
    L = requests.get(Url+"GBP")
    Text = L.text
    Valor = json.loads(Text)
    Libra = Valor.get("GBP").get("high")
    
    return Libra
    
def Yene():
    Y = requests.get(Url+"JPY")  
    Text = Y.text
    Valor = json.loads(Text)
    Yene = Valor.get("JPY").get("high")
    
    return Yene
      
print(Yene())