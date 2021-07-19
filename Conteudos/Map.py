#E um método que intera todos os elementos do array 
#Sem a necessidade expressiva de usar uma estrutura de repetição
#E necessário usar list antes do map e apresentar 2 paramentros
#Uma função e um e um interavel(array)
#É interessante usar só um paramento na sua função
Vetor = [1,2,3,4]
def Multi(b):
    return 10 * b

Variavel = list(map(lambda x: x * 10, Vetor))
print(Variavel)