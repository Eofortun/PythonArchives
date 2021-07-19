from Chamaveis import Local, Barras
import codecs, os

B1 = Barras.BarraDupla

Local_dir = Local.Local_dir(__file__)
Local_files = os.listdir(Local_dir)
#Filter_local = list(filter(lambda x: ".txt" in x, Local_files))

B1()
for x in range(len(Local_files)):
    print(f"[{x}] = {Local_files[x]}")
B1()
while True:
    Escolha = int(input("Eacolha: "))
    if Escolha >= 0 and Escolha < len(Local_files):
        break
B1()

select_file = Local_dir + Local_files[Escolha]
print("Caminho Local: ", select_file)

B1()

try:
    a = codecs.lookup(select_file)
    print(a)
    
except LookupError:
    print("Codec não encontrado")