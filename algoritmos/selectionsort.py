lista = [75, 12, 7, 8, 36]

def selection_sort(lista):
    for actual in range(len(lista) - 1):
        min_id = actual
        for i in range(actual, len(lista)):
            if lista[min_id] > lista[i]:
                print(f"{lista[min_id]} maior que {lista[i]}")
                min_id = i

        if lista[actual] > lista[min_id]:
            aux = lista[actual] 
            lista[actual] = lista[min_id]
            lista[min_id] = aux
    return lista

print(selection_sort(lista))
