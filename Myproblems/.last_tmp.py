from Chamaveis import Local, All_files
from functools import reduce

Local = Local.Local_dir(__file__)
Search = All_files.FindFiles(Local)
All_files.ShowFiles(Search)
Escolha = int(input("Escolha: "))

Ignore = ['"', '.', ',' " "]
print(Local+Search[Escolha])
with open(Local+Search[Escolha], "r") as File:
    Ler = File.read()
    ReduzidoA = len(list(filter(lambda x: x != Ignore, Ler)))
    print(ReduzidoA)
    """
    Cont = 0
    for w in range(0,len(Ignore)):
        for x in range(0,len(Ler)):
            if Ignore[w] != Ler[x]:
                Texto += Ler[x]
    print(Cont)"""