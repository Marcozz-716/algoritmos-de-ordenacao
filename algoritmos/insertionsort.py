lista = [4, 7, 2, 5, 4, 0]

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        anterior_id = i - 1
        while anterior_id >= 0 and lista[anterior_id] > chave:
            lista[anterior_id + 1], lista[anterior_id] = lista[anterior_id], lista[anterior_id + 1]
            anterior_id -= 1
    return lista

print(insertion_sort(lista))
