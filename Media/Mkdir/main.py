from Chamaveis import Barras, Local, ArquivoCreator
import sys, os

B1 = Barras.BarraDupla
B1()
print("{CRIANDO DIRETÓRIOS}".center(38,"="))
B1()

path = Local.Local_dir(__file__)
a = "/storage/emulated/0/qpython/Mundo2/Arquivos/Mkdir"
ArquivoCreator.standard(path,".txt",a)

# CRIA UM DIRETORIO

Pathdir = os.path.join(a, "New")#Juntar Um caminho já criado + "Nome da pasta"

os.mkdir(Pathdir)