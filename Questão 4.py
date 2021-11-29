def dados():
    num = 12
    nome = []
    altura = []
    cont = 0
    while cont < num:
        nome_paraInserir = input().strip()
        altura_paraInserir = float(input())
        nome.append(nome_paraInserir)
        altura.append(altura_paraInserir)
        cont += 1
    return nome, altura


def maior(nomes, alturas):
    indice_mais_alto = alturas.index(max(alturas))
    return nomes[indice_mais_alto], alturas[indice_mais_alto]


def media_aritimetrica(lista):
    tam = len(lista)
    i = 0
    total = 0
    while i < tam:
        total += lista[i]
        i += 1
    return total / tam


def acima_da_media(media, nomes, alturas):
    Nomes_acimaDaMedia = []
    alturas_acimaDaMedia = []
    tam = len(alturas)
    i = 0
    total = 0
    while i < tam:
        if alturas[i] > media:
            Nomes_acimaDaMedia.append(nomes[i])
            alturas_acimaDaMedia.append(alturas[i])
        i += 1

    return Nomes_acimaDaMedia, alturas_acimaDaMedia


def main():
   
    nome_atletas, altura_atletas = dados()

    
    nome_jogador_mais_alto, altura_jogador_mais_alto = maior(nome_atletas, altura_atletas)
    media_das_alturas = media_aritimetrica(altura_atletas)
    atletas_acima_da_mediaNomes, atletas_acima_da_mediaAlturas = acima_da_media(media_das_alturas, nome_atletas, altura_atletas)

    
    print('JOGADOR MAIS ALTO DO TIME')
    print(f'{nome_jogador_mais_alto}')
    print(f'{altura_jogador_mais_alto:.2f}')
    print('ALTURA MÉDIA DO TIME')
    print(f'{media_das_alturas:.2f}')
    print('JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')

    tam = len(atletas_acima_da_mediaNomes)
    i = 0
    total = 0
    while i < tam:
        print(atletas_acima_da_mediaNomes[i])
        print(f'{atletas_acima_da_mediaAlturas[i]:.2f}')
        i += 1


if __name__ == '__main__':
    main()
