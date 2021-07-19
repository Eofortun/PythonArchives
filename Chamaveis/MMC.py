
#print("Valor: ", Valor)
'''
Vetor = []

for x in range(2,Valor):
    for y in range(1, Valor):
        if(x * y) == Valor:
            if((x * y) % 2) == 1 or ((x * y) % 2) == 0:
                #fazer uma função que verifique se o valor de % == 1 caso sim chame uma função que retorne um numero q possa ser dividido da maneira correta
                print(f'Normal: {x} × {y} = {x*y}')
                Vetor.append(f'{x} × {y} = {x*y}')
                break
        elif((x * y) + 1) == Valor:
            print(f'Mais 1: {x} × {y} + 1 = {(x*y)}PAR')
            break
            
print(Vetor)
'''
'''
def MMC(Valor):
    ProxValor = []
    for x in range(2, Valor):
        for y in range(Valor):        
           
            if(x * y) == Valor and (x * y) % 2 == 0:
                ProxValor.append(f'N:{x}')
                #	print(f'N: {x} × {y} = {x * y}')#Normal
            elif(x * y)+1 == Valor and ((x * y)+1) % 2 == 1:
                ProxValor.append(f'P:{x}')
                	#f'P: {x} × {y} = {x * y}')#Mais 1
               
    return ProxValor
Valor = 90
print("Valor: ", Valor)    
print("MMC:", MMC(Valor))
'''
def Sample(V):
    NeuValue0 = round(V / 2)
    if NeuValue0 * 2 == V:
        return 0        
    elif ((NeuValue0 * 2) + 1) == V or ((NeuValue0 * 2) - 1) == V:        
        return -1
            
Valor = 2
print('Valor: ', Valor)
#print('Me:', round(11 / 2))           
print('Machine:', Sample(Valor))
print("-="*15)
Matriz = [Valor]
Contador = True
while Contador:
    Fvalor = Sample(Valor) 
    print(f"Fvalor: {Valor} + ({Fvalor})")
    Valor = round((Valor + Fvalor)/2)
    print("Valor: ", Valor)
    Matriz.append(Valor)    
    if Valor == 1:
        Contador = False
print("-=" * 15)
print('Matriz: ', Matriz)
#Matriz.append(1)
Binario = []
for z in range(len(Matriz)):
    Binario.append(f'{Matriz[z]%2}')
    
Retorno = ''
for LenBin in range(len(Binario)):
    Retorno += Binario[LenBin]

print("NBinario: ", Retorno)
print("RBinario: ", Retorno[::-1],'*B')
    





                    