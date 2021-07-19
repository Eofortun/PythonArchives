from Chamaveis import Barras
import requests
import json

B1 = Barras.BarraDupla

B1()
print("《CEP VERIFICATOR》".center(38,"="))
B1() 

r = requests.get('http://economia.awesomeapi.com.br/json/all/USD')
Sample = r.text
#r.encoding = 'ISO-8859-1'#Codifica o texto em ISO
#Ve qual a codificação de r
#print(type(Sample))Verifica o tipo de Sample
y = json.loads(Sample)#Carrega o aquivo Json, para que possa acessar seus conteudos
print(Sample)
B1()
print(y.get("USD").get("high"))#Entra dentro do diretorio "USD", com .get adentra mais ainda no codigo

