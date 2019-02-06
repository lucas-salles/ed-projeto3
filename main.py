import random
import time

# BubbleSort
def bubbleSort(lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                ordenado = False
    return lista


# SelectionSort
def selectionSort(lista):
    for i in range(len(lista)-1, 0, -1):
        positionOfMax = 0
        for j in range(1, i+1):
            if lista[j] > lista[positionOfMax]:
                positionOfMax = j

        temp = lista[i]
        lista[i] = lista[positionOfMax]
        lista[positionOfMax] = temp


# InsertionSort
def insertionSort(lista):
    for i in range(1, len(lista)):

        currentvalue = lista[i]
        position = i

        while position > 0 and lista[position-1] > currentvalue:
            lista[position] = lista[position-1]
            position = position-1

        lista[position] = currentvalue


# ShellSort
def shellSort(lista):
    sublistcount = len(lista)//2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(lista, startposition, sublistcount)

        sublistcount = sublistcount // 2

def gapInsertionSort(lista, start, gap):
    for i in range(start+gap, len(lista), gap):

        currentvalue = lista[i]
        position = i

        while position >= gap and lista[position-gap] > currentvalue:
            lista[position] = lista[position-gap]
            position = position-gap

        lista[position] = currentvalue


# QuickSort
def quickSort(lista):
    quickSortHelper(lista, 0, len(lista)-1)

def quickSortHelper(lista, first, last):
    if first < last:

        splitpoint = partition(lista, first, last)

        quickSortHelper(lista, first, splitpoint-1)
        quickSortHelper(lista, splitpoint+1, last)

def partition(lista, first, last):
    pivotvalue = lista[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and lista[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while lista[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = lista[leftmark]
            lista[leftmark] = lista[rightmark]
            lista[rightmark] = temp

    temp = lista[first]
    lista[first] = lista[rightmark]
    lista[rightmark] = temp

    return rightmark


# MergeSort
def mergeSort(lista):
    if len(lista) > 1:
        mid = len(lista)//2
        lefthalf = lista[:mid]
        righthalf = lista[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                lista[k] = lefthalf[i]
                i = i+1
            else:
                lista[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            lista[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            lista[k] = righthalf[j]
            j = j+1
            k = k+1



# Criando lista e gerando chaves randomicamente
chave = []
for i in range(1000):
    chave.append(random.randint(1, 5000))


# Medindo o tempo do BubbleSort
lista1 = []
for i in range(len(chave)):
    lista1.append(chave[i])

inicio = time.time()
bubbleSort(lista1)
fim = time.time()
buble_sort = fim - inicio



# Medindo o tempo do SelectionSort
lista2 = []
for i in range(len(chave)):
    lista2.append(chave[i])

inicio = time.time()
selectionSort(lista2)
fim = time.time()
selection_sort = fim - inicio



# Medindo o tempo do InsertionSort
lista3 = []
for i in range(len(chave)):
    lista3.append(chave[i])

inicio = time.time()
insertionSort(lista3)
fim = time.time()
insertion_sort = fim - inicio



# Medindo o tempo do ShellSort
lista4 = []
for i in range(len(chave)):
    lista4.append(chave[i])

inicio = time.time()
shellSort(lista4)
fim = time.time()
shell_sort = fim - inicio



# Medindo o tempo do QuickSort
lista5 = []
for i in range(len(chave)):
    lista5.append(chave[i])

inicio = time.time()
quickSort(lista5)
fim = time.time()
quick_sort = fim - inicio



# Medindo o tempo do MergeSort
lista6 = []
for i in range(len(chave)):
    lista6.append(chave[i])
inicio = time.time()
mergeSort(lista6)
fim = time.time()
merge_sort = fim - inicio


print('-='*8 + 'Resultado' + '-='*8)
print('Bubble Sort: {:.5f} s'.format(buble_sort))
print('Selection Sort: {:.5f} s'.format(selection_sort))
print('Insertion Sort: {:.5f} s'.format(insertion_sort))
print('Shell Sort: {:.5f} s'.format(shell_sort))
print('Quick Sort: {:.5f} s'.format(quick_sort))
print('Merge Sort: {:.5f} s'.format(merge_sort))
print('-='*20)
