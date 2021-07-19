from Chamaveis import Barras
import Local
import os

B1 = Barras.BarraDupla
B1()
print("《MAKE A DIRECTORY》".center(38,"="))
B1()
Nome_Dir = str(input("Nome: "))
path = Local.LocalLess(__file__)

Vetor_Dir = os.listdir(path)

path = path + "/" + Nome_Dir

#print("Paths: ", Vetor_Dir)
#print("Nome_Dir: ", Nome_Dir)

B1()
Relé = list(filter(lambda x: Nome_Dir == x, Vetor_Dir))
if len(Relé) == 0:
    os.mkdir(path)
    print("Pasta Criada")
    print("Path: ", path)
else:
    print("Arquivo Já existe")
    exit()
B1()