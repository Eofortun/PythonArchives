B1 = lambda x=20: print("-="*x)
B1()
print("《FIBONACCI》".center(38))
B1()
Valor = int(input("Valor: "))

Valor1 = 0
Valor2 = 1
Total = 0

Cont = 0
Continuar = True
while Continuar:
    print(Total)
    Valor1 = Valor2
    Valor2 = Total
    Total = Valor1 + Valor2
    
    Cont += 1
    if Cont == Valor:               
        Continuar = False
B1()
print("《FIM》".center(38,"="))
B1()