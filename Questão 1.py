def criaLista():
    lista = []
    while True:
        n = int(input())
        if n == 0:
            break
        lista.append(n)

    return lista


def comprimento(lista):
    tem = True
    cont = 0
    i = 0
    while True:
        try:
            if lista[i] != '':
                cont += 1
            i += 1
        except:
            break
    return cont


def inverter(lista):
    tamanho = comprimento(lista)
    lista_invertida = []
    i = 0
    while i < tamanho:
        lista_invertida.insert(0, lista[i])
        i += 1

    return lista_invertida


def minimo(lista):
    tamanho = comprimento(lista)
    i = 1
    minimo = lista[0]
    while i < tamanho:
        if lista[i] < minimo:
            minimo = lista[i]
        i += 1
    return minimo


def maximo(lista):
    tamanho = comprimento(lista)
    i = 1
    maximo = lista[0]
    while i < tamanho:
        if lista[i] > maximo:
            maximo = lista[i]
        i += 1
    return maximo


def soma(lista):
    tamanho = comprimento(lista)
    i = 0
    soma = 0
    while i < tamanho:
        soma += int(lista[i])
        i += 1
    return soma


def main():

    lista1 = criaLista()

    comprimento_lista1 = comprimento(lista1)
    lista2_invertida = inverter(lista1)

    try:
        minimo_lista3 = minimo(lista1)
    except:
        minimo_lista3 = 0

    try:
        maior_lista4 = maximo(lista1)
    except:
        maior_lista4 = 0

    soma_itens_lista = soma(lista1)

    print(f'{lista1}')
    print(f'{comprimento_lista1}')
    print(f'{lista2_invertida}')
    print(f'{minimo_lista3}')
    print(f'{maior_lista4}')
    print(f'{soma_itens_lista}')


if __name__ == '__main__':
    main()
