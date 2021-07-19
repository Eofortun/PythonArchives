#Lambda são funções anônimas tais quais a do javascript
# Elas podem receber parâmetros, funções exteriores
def Multiplicador(a,b):
    return a * b
A = lambda x,y: print(x * y)
A(10, Multiplicador(3,3))