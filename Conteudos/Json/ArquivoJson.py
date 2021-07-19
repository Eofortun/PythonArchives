from functools import reduce
import json, os

#Retorna o caminho do arquivo local
Local = __file__
Vetor = Local.split("/")
Vetor.pop()

#Aficionada as "/" conforme necessario
Total = "/"
Total += reduce(lambda x, y: x + y + "/",Vetor)

print("Total: ", Total)

#Crindo novo arquivo JSON: mudar a extensão do arquivo txt

Arquivo = str(input("Nome do arquivo: "))
Arquivo += ".txt"
Json = open(Total+Arquivo, "w")
print(Total+Arquivo)

Dir = os.listdir(Total)
Dir_have = list(filter(lambda a: a == Dir, Total))

Json.write(str(input("Texto: ")))
Json.close()

#Verifica se o arquivo foi criado!
if Dir_have != 0:
    print("Arquivo Criado!")
else:
    print("Arquivo não Criado!")


