#Forma mais simple de ordenação dos elementos
#É necessário usar "fstring"

print()
Título = "《LOREM IPSUM》"
print(f"{Título:-^40}")#Centro
print(f"{Título:-<40}")#Esquerda 
print(f"{Título:->40}")#Direita

print()

Barra = "|"
Barra1 = ""
print(f"{Barra1:-^41}")
print("《ESTRUTURA DE BARRAS》".center(40))
print(f"{Barra1:-^41}")
for x in range(10):
    print(f"{Barra:<}{Barra: >40}")
print(f"{Barra1:-^41}")