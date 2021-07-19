from Chamaveis import Barras
from functools import reduce
Produtos = {}
B1 = Barras.BarraDupla

B1()
print("《♤MERCADINHO_DA_ESQUINA♤》".center(38, "="))
B1()

while True:
    Nome = str(input("Nome do Produto: "))
    Price = float(input("Valor do Produto: R$"))
    
    Produtos[Nome] = Price 
   
    B1()
    
    Continue = str(input("Deseja continuar[S/N]: ")).upper()
    if Continue == "N":
        break
    
    B1()

Valor = list(Produtos.values())#Para transformar de dict em list sem o uso do for
Chave = list(Produtos.keys())
print("Keys: ", Chave)
print("Values: ", Valor)
Menor = reduce(lambda x, y: x if x < y else y, Valor)
Total = reduce(lambda x, y: x+y, Valor)
Plus = list(filter(lambda x: x > 1000, Valor))

IndiceX = 0
for x in range(0,len(Valor)):
    if Menor == Valor[x]:
        IndiceX = x
        break

IndiceY = 0
for y in range(0, len(Valor)):
    if Menor == Valor[y]:
        IndiceY = y

print("Item: ", Chave[IndiceX])
print("Total: ",Total)
print("Menor Produto: ", Chave[IndiceY])
