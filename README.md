# Algoritmos de Ordenação
Estudar algoritmos de ordenação, apesar de parecer algo teórico demais, pode melhorar nossa lógica de programação e nos ajudar a escolher o melhor algoritmo pra lidar com dados específicos.

Nesse repositório eu irei falar sobre os algoritmos:\
**Selection Sort**\
**Bubble Sort**\
**Insertion Sort**\
**Merge Sort**\
**Quick Sort**

Você pode verificar a implementação dos algoritmos nessa [pasta](https://github.com/Marcozz-716/algoritmos-de-ordenacao/tree/main/algoritmos)

## Selection Sort
O Selection Sort funciona dividindo os dados em duas partes: ordenados e não ordenados. Ele busca o menor elemento do conjunto, colocando-o no início e avançando para a direita para ordenar os demais elementos. 

O fluxo é basicamente:\
**1 - Encontrar o elemento mínimo entre os dados**
```
lista = [75, 12, 7, 8, 36]
menor_elemento_id = 0
for i in range(len(lista)):
    if lista[i] < lista[menor_elemento_id]:
        menor_elemento_id = i
```
</br>
**2 - Trocar o elemento mínimo encontrado com o elemento de primeiro índice**
```
lista = [75, 12, 7, 8, 36]
menor_elemento_id = 0
for i in range(len(lista)):
    if lista[i] < lista[menor_elemento_id]:
        menor_elemento_id = i
limite = 0
# Trocando a ordem
if lista[limite] > lista[menor_elemento_id]:
    var_aux = lista[limite]
    lista[limite] = lista[menor_elemento_id]
    lista[menor_elemento_id] = var_aux
```
</br>
**3 - Mover o limite para a direita e repetir até ordenar tudo**
```
    lista = [75, 12, 7, 8, 36]
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
    return lista```
</br>

### Vantagens do Selection Sort: 
Fácil de implementar e funciona bem para listas pequenas
### Desvantagens do Selection Sort: 
Não é tão eficiente pra listas grandes