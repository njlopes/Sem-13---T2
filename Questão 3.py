def dados():
    num = 20
    lista = []
    cont = 0
    while cont < num:
        n_paraInserir = int(input())
        lista.append(n_paraInserir)
        cont += 1
    return lista


def intercalaçao(listaA, listaB):
    num = 20
    cont = 0
    listaC = []
    while cont < num:
        itemToInsert = listaA[cont] + listaB[cont]
        listaC.append(itemToInsert)
        cont += 1
    return listaC


def main():
    listaA = dados()
    listaB = dados()

   
    listaC = intercalaçao(listaA, listaB)

  
    print(f'{listaA}')
    print(f'{listaB}')
    print(f'{listaC}')


if __name__ == '__main__':
    main()
