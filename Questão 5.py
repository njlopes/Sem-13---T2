def dados():
    num = 30
    nome = []
    idade = []
    altura = []
    cont = 0
    while cont < num:
        nome_paraInserir = input().strip()
        idade_paraInserir = int(input())
        altura_paraInserir = float(input())
        nome.append(nome_paraInserir)
        idade.append(idade_paraInserir)
        altura.append(round(altura_paraInserir, 2))
        cont += 1
    return nome, idade, altura


def media_aritimetrica(lista):
    tam = len(lista)
    i = 0
    total = 0
    while i < tam:
        total += lista[i]
        i += 1
    return round(total / tam, 2)


def alunosMenores(media_alturas, nomes, idades, alturas):
    Nomes_abaixoDaMedia = []
    alturas_abaixoDaMedia = []
    idade_doAluno = []
    tam = len(nomes)
    i = 0
    total = 0
    while i < tam:
        if idades[i] > 13:
            if alturas[i] < media_alturas:
                Nomes_abaixoDaMedia.append(nomes[i])
                alturas_abaixoDaMedia.append(alturas[i])
                idade_doAluno.append(idades[i])
        i += 1
    return Nomes_abaixoDaMedia, alturas_abaixoDaMedia, idade_doAluno


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
    nome_alunos, idade_alunos, altura_alunos = dados()
    media_alturas = media_aritimetrica(altura_alunos)
    nome_maior_de13_inferiroAmediaAlt, altura_maior_de13_inferiroAmediaAlt, idade_maior_de13_inferiroAmediaAlt = alunosMenores(media_alturas, nome_alunos, idade_alunos, altura_alunos)

    print('MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA')
    tam = len(nome_maior_de13_inferiroAmediaAlt)
    i = 0
    total = 0
    while i < tam:
        print(nome_maior_de13_inferiroAmediaAlt[i])
        i += 1


if __name__ == '__main__':
    main()
