def quick_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1

    if inicio < fim:
        p = partition(lista, inicio, fim) # posição do pivô após a "centralização"
        quick_sort(lista, inicio, p-1) # esquerda, com os itens menores que o pivô
        quick_sort(lista, p+1, fim) # direita, com os itens maiores
    return lista

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i += 1

    lista[fim], lista[i] = lista[i], lista[fim]
    return i

lista = [89, 13, 17, 8, 5, 54]
print(quick_sort(lista))




