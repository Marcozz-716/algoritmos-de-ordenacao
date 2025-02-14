import random

#lista = random.sample(range(1, 100), 20)

lista = [4, 9, 2, 1, 7, 8]

def bubble_sort(lista):
    for i in range(len(lista) - 1):
        if lista[i+1] < lista[i]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista

def bubble_sort2(lista):
    for _ in range(len(lista) - 1):
        for i in range(len(lista) - 1):
            if lista[i+1] < lista[i]:
                lista[i], lista[i+1] = lista[i+1], lista[i] # troca sem variável auxiliar
    return lista


print(bubble_sort(lista=lista))