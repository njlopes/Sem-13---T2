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


def contem(lista, valor_pesquisa):
    tamanho = comprimento(lista)
    i = 0
    tem = 0
    while i < tamanho:
        if valor_pesquisa == lista[i]:
            tem += 1
        i += 1
    return tem


def main():
    lista = criaLista()
    valor_pesquisa = int(input())

    tem_na_lista = contem(lista, valor_pesquisa)

    print(f'{lista}')
    print(f'{valor_pesquisa}')
    print(f'{tem_na_lista}')


if __name__ == '__main__':
    main()
