def BinToDec(bin):
    #/////// TRANSFORMA O (BIN)ARIO EM STRING E INVERTE
    Elemento = str(bin)[::-1]#Pega o tamanho do valor decimal e adiciona no array
    #//////////////////////////
    
    #/////// FRAGMENTA A STRING ELEMENTO E GUARDA-O NA ARRAY EM FORMA DE INTEIRO
    DecimalSize = []
    for i in range(len(Elemento)):
        DecimalSize.append(int(Elemento[i]))
        
    #////////////////////////////
    	
    #////// CALCULA A POTENCIA DE 2 × O VALOR, RETORNA O VALOR DECIMAL
    def Binario(valor):
        C = 0
        V = 0
        for x in range(len(valor)):
            C += valor[x] * pow(2, V)
            #print("valor: ",valor[x],"pow: ", pow(2, V),"total: ", valor[x] * pow(2, V))
            V += 1
        return C
    return Binario(DecimalSize)

def DecToBin(V):
    #Faz a conversão de um número decimal para Binário;
    #////// VERIFICA SE O N° É INTEIRO OU NÃO, RETORNA 0 CASO SEJA E -1 SENÃO FOR
    def Sample(Vd):
        NeuValue0 = round(Vd / 2)
        if NeuValue0 * 2 == Vd:
            return 0        
        elif ((NeuValue0 * 2) + 1) == Vd or ((NeuValue0 * 2) - 1) == Vd:        
            return -1
    #////////////////////////////////////////////        
   
   #/////// FAZ O MMMC ////////
    Valor = V
    Matriz = [Valor]
    Contador = True
    while Contador:
        Fvalor = Sample(Valor) 
        Valor = round((Valor + Fvalor)/2)
        Matriz.append(Valor)    
        if Valor == 1:
            Contador = False
    #////////////////////////////
    
    #///// TRANSFORMA OS ELEMENTOS E UMA STRING E RETORNA ELA INVERTIDA
    Binario = []
    for z in range(len(Matriz)):
        Binario.append(f'{Matriz[z]%2}')
        
    Retorno = ''
    for LenBin in range(len(Binario)):
        Retorno += Binario[LenBin]
    return Retorno[::-1]
    #/////////////////////////////////////
    



    
