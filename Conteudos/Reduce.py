#Reduce retorna um valor só, caso deseje somar todos os valores do vetor é ele que 
#você deve usar. É necessário importalo do funtools, e diferente do filter e map
#ele não precisa do list na frente.
from functools import reduce
Vetor = [1,2,3,4,5,6,7,8,9]
Elemento = reduce(lambda x, y: x*y, range(1,10))
print(Elemento)