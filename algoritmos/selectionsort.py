lista = [5, 4, 3, 2, 1]

def sort2(lista):
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

print(sort2(lista))