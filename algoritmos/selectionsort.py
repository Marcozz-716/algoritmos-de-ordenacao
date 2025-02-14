lista = [75, 12, 7, 8, 36]

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

#print(sort2(lista))
menor_elemento_id = 0
for i in range(len(lista)):
    if lista[i] < lista[menor_elemento_id]:
        menor_elemento_id = i
ultimo_ordenado_id = 0
if lista[ultimo_ordenado_id] > lista[menor_elemento_id]:
    var_aux = lista[ultimo_ordenado_id]
    lista[ultimo_ordenado_id] = lista[menor_elemento_id]
    lista[menor_elemento_id] = var_aux

print(lista)