def Num(Valor):#Beta
   from functools import reduce
   Num = [0,1,2,3,4,5,6,7,8,9]
   Array = list(filter(lambda x: str(x), Valor))   
   IsNum = []
   for x in range(len(Valor)):
       if Valor[x] in str(Num):
           IsNum.append(Valor[x])
   if IsNum == Array:
       return 1
   else: 
       return 0


