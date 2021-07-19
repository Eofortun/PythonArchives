#Função Filter ajuda a filtrar o valor caso seja Verdadeiro
#esse procedimento retorna somente True
Vetor = [1,2,3,4,5]
def ParOuImpar(X):
    if X % 2 == 0:
        return True

Filtro = list(filter(lambda x: x % 2 == 0, Vetor))
print("Array: ", Vetor)
print("Filtrado: ", Filtro)