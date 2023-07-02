from random import randrange


def jogar():
    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta("palavras.txt")  # Carrega a palavra secreta do arquivo "palavras.txt"
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)  # Inicializa uma lista com underscores para representar as letras acertadas
    print(letras_acertadas)

    enforcou = False  # Variável para verificar se o jogador foi enforcado
    acertou = False  # Variável para verificar se o jogador acertou a palavra
    erros = 0  # Contador de erros

    while not enforcou and not acertou:
        chute = inicializa_chute()  # Obtém uma letra do jogador

        if chute in palavra_secreta:  # Verifica se a letra está na palavra secreta
            marca_chute_correto(palavra_secreta, letras_acertadas, chute)  # Marca o chute correto na lista de letras acertadas
        else:
            erros += 1  # Incrementa o número de erros
            desenha_forca(erros)  # Desenha a forca correspondente ao número de erros

        acertou = "_" not in letras_acertadas  # Verifica se todas as letras foram acertadas
        enforcou = erros == 7  # Verifica se o número de erros chegou a 7
        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


def desenha_forca(erros):
    """
    Desenha a forca correspondente ao número de erros.

    Args:
        erros (int): Número de erros do jogador.
    """
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_mensagem_perdedor(palavra_secreta):
    """
    Imprime a mensagem de perdedor quando o jogador é enforcado.

    Args:
        palavra_secreta (str): Palavra secreta que o jogador não conseguiu adivinhar.
    """
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    """
    Imprime a mensagem de vencedor quando o jogador acerta a palavra.
    """
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def marca_chute_correto(palavra_secreta, letras_acertadas, chute):
    """
    Marca o chute correto na lista de letras acertadas.

    Args:
        palavra_secreta (str): Palavra secreta.
        letras_acertadas (list): Lista de letras acertadas.
        chute (str): Chute do jogador.
    """
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def inicializa_chute():
    """
    Inicializa o chute do jogador.

    Returns:
        str: Chute do jogador.
    """
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute


def inicializa_letras_acertadas(palavra_secreta):
    """
    Inicializa a lista de letras acertadas com underscores.

    Args:
        palavra_secreta (str): Palavra secreta.

    Returns:
        list: Lista de letras acertadas.
    """
    return ["_" for letra in palavra_secreta]


def imprime_mensagem_abertura():
    """
    Imprime a mensagem de abertura do jogo.
    """
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carrega_palavra_secreta(nome_arquivo="palavras.txt"):
    """
    Carrega uma palavra secreta do arquivo.

    Args:
        nome_arquivo (str): Nome do arquivo de palavras (padrão: "palavras.txt").

    Returns:
        str: Palavra secreta.
    """
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        palavras = []
        for linha in arquivo:
            palavras.append(linha.strip())

    numero = randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


if __name__ == "__main__":
    jogar()
