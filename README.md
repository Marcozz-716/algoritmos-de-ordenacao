# algoritmos de ordenacao
Estudar algoritmos de ordenação, apesar de parecer algo teórico demais, pode melhorar nossa lógica de programação e nos ajudar a escolher o melhor algoritmo pra lidar com dados específicos.

Nesse repositório eu irei falar sobre os algoritmos:\
**Selection Sort**\
**Bubble Sort**\
**Insertion Sort**\
**Merge Sort**\
**Quick Sort**

Você pode verificar a implementação dos algoritmos nessa [pasta](https://github.com/Marcozz-716/algoritmos-de-ordenacao/tree/main/algoritmos)

## Selection Sort
O Selection Sort funciona dividindo os dados em duas partes: ordenados e não ordenados. Ele busca o menor elemento do conjunto, colocando-o no início do conjunto e avançando para a direita para ordenar os demais elementos. 

O fluxo é basicamente:\
**1 - Encontrar o elemento mínimo entre os dados**\
```
for actual in range(len(lista) - 1):
    min_id = actual
    for i in range(actual, len(lista)):
        if lista[min_id] > lista[i]:
            print(f"{lista[min_id]} maior que {lista[i]}")
            min_id = i
```</br>
**2 - Trocar o elemento mínimo encontrado com o elemento de primeiro índice**
****