def selectionSort(lista):
   for i in range(len(lista)-1,0,-1):
       positionOfMax=0
       for j in range(1,i+1):
           if lista[j]>lista[positionOfMax]:
               positionOfMax = j

       temp = lista[i]
       lista[i] = lista[positionOfMax]
       lista[positionOfMax] = temp