from Chamaveis import Barras, Local
import os, json

B1 = Barras.BarraDupla
Local = Local.Local_dir(__file__)
Diretorio = os.listdir(Local)

#print(Diretorio)
#print(Local)

#Retorna um Array com todos os arquivos .json
Arquivos_json = list(filter(lambda x: ".json" in x , Diretorio)) 
#print(Arquivos_json)

B1()
print("《LEITOR JSON》".center(38,"="))
B1()
for beta in range(len(Arquivos_json)):
    print(f"{[beta]} = {Arquivos_json[beta]}")
B1()

#Verifica se o dado condiz com a lista de escolhas
Choice = int(input("Escolha: "))
#print(Arquivos_json[Choice])
X = Local+Arquivos_json[Choice]
#print(X)

B1()
with open(X, "r") as Json_Transform:
    txt = json.load(Json_Transform)
    print(txt)

    