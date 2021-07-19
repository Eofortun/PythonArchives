from Chamaveis import Barras
from functools import reduce
import os
Caminho = os.path.dirname(os.path.realpath(__file__))#Diretorio
print(Caminho)

B1 = Barras.BarraDupla

B1()
'''
@ Cria um nome arquivo.txt
'''
print("《VERIFICADOR DE ARQUIVO.TXT》".center(38,"="))

B1()

arquivo = str(input("Nome do arquivo: "))
arquivoP = arquivo+".txt"

Nov = Caminho+"/"

Url = os.listdir(Caminho)

'''
@ Filtro before: verifica se o arquivo 
@ solicitado, ja foi criado.'''

FilterB = list(filter(lambda X: X == arquivoP, Url))

if len(FilterB) == 0:
    V = open(Nov+arquivoP , "w")
    V.write(input("Texto do arquivo: "))    
    V.close()
    B1()
    Url = os.listdir(Caminho)
    FilterA = list(filter(lambda X: X == arquivoP, Url))
    print("Arquivo criado: ", True if len(FilterA) != 0 else False)
else:
    B1()
    print("Arquivo já existente")
    print("Arquivo não criado!")
  

'''
@ Verifica se o arquivo.txt foi criado corretamente 
@ no repositorio atual!
'''

