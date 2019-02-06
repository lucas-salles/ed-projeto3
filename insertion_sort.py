def insertionSort(lista):
   for i in range(1,len(lista)):

     currentvalue = lista[i]
     position = i

     while position>0 and lista[position-1]>currentvalue:
         lista[position]=lista[position-1]
         position = position-1

     lista[position] = currentvalue