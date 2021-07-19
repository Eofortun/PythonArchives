from Chamaveis import Barras as B
from Chamaveis import Local as L
#O "as" é como =, que recebe a variavel
B1 = B.BarraDupla
B1()
Localdir = L.Local_dir(__file__)
print(Localdir)
Arquivo = Localdir+"Fantástico.txt"

"""
#Modo correto sem with
try:
    f = open(Arquivo, "w")
finally:
    f.close()
print(f)

#Modo correto com with
with open(Arquivo, "w") as T:
    T.write(Arquivo)

#Modo incorreto!
v = open(Arquivo, "w")
v.close()
"""