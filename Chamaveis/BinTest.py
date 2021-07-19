Vetor = []
x = 0
V = 23
while x < 10:
    #Vetor.append(round(V % 2))
    
    print(x, '°: ', V, V % 2)
    V = round(V / 2)
    x += 1


print(Vetor)