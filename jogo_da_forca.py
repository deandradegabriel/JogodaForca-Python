
import os
import random
import unicodedata

os.system('cls')

print('===============================================')
print('        SEJA BEM-VINDO AO JOGO DA FORCA')
print('===============================================\n')


regras = [
    ' 1. Digite apenas uma letra por vez.',
    ' 2. Só são aceitas letras como tentativa.',
    ' 3. Não são aceitas letras repetidas.',
    ' 4. A cada tentativa errada, uma parte do boneco é acrescentada à forca,\
    \n (Caso forme o corpo completo, o jogador perde.).'
]

lista_palavras = [
    'python',
    'palavra',
    'escolha',
    'computador',
    'trabalho',
    'coração',
    'árvore',
    'programação',
    'informação',
    'função'
]



# -----------------------------------------------------------------------------
#                      === Principais funções do Jogo ===
# -----------------------------------------------------------------------------

def NormalizarAcentos(texto):
    texto = unicodedata.normalize('NFD', texto)

    texto = ''.join(
        caractere
        for caractere in texto
        if unicodedata.category(caractere) != 'Mn'
    )

    return texto


def MostrarRegras():
    print('Regras do jogo:')

    for regra in regras:
        print(regra)


def FormatoPalavraEscondida(palavra):
    n_letras_secretas = ''

    for _ in palavra:
        n_letras_secretas += '_'

    print(f'\nPalavra secreta: {n_letras_secretas}')


def LerLetra():
    while True:
        letra = input('Digite uma letra: ').lower()

        print('------------------------------------------------')

        if len(letra) != 1:
            print(
                "\nErro! Você infringiu a regra:\n"
                f"{regras[0]}\n"
                "Tente novamente!\n"
            )
            continue

        if not letra.isalpha():
            print(
                "\nErro! Você infringiu a regra:\n"
                f"{regras[1]}\n"
                "Tente novamente!\n"
            )
            continue

        return letra


def LetraRepetida(letra, letras_tentadas):
    letra_normalizada = NormalizarAcentos(letra)

    for letra_tentada in letras_tentadas:
        if NormalizarAcentos(letra_tentada) == letra_normalizada:
            return True

    return False


def MontarPalavraAtual(palavra, letras_tentadas):
    palavra_atual = ''

    for letra in palavra:

        letra_encontrada = False

        for letra_tentada in letras_tentadas:
            if NormalizarAcentos(letra_tentada) == NormalizarAcentos(letra):
                letra_encontrada = True
                break

        if letra_encontrada:
            palavra_atual += letra
        else:
            palavra_atual += '_'

    return palavra_atual


def MostrarCorpo(tentativas_erradas):
    partes_corpo = [
        'Cabeça',
        'Tronco',
        'Braços',
        'Pernas'
    ]

    corpo_formado = partes_corpo[:tentativas_erradas]

    if corpo_formado:
        print(f"Corpo na forca: {', '.join(corpo_formado)}\n")
    else:
        print('Corpo na forca: nenhuma parte formada\n')


def Perdeu(tentativas_erradas, maximo_erros, palavra_revelada):
    if tentativas_erradas >= maximo_erros:
        print('Número de erros excedidos, o corpo na forca foi completado!\n'
              'VOCÊ PERDEU!!!')
        print(f'A palavra secreta era: {palavra_revelada}')

        return True

    return False


def Venceu(palavra_atual, palavra_escondida):
    return palavra_atual == palavra_escondida


def ContinuarOuPararJogo():
    while True:
        pergunta_de_saida = input(
            'Deseja continuar jogando (Sim/Não)? '
        ).lower()

        if pergunta_de_saida == 'não' or pergunta_de_saida == 'nao':
            print('Você saiu!!!')
            return False

        elif pergunta_de_saida == 'sim':
            print('Carregando novamente o jogo...\n')
            return True

        else:
            print('Resposta inválida!!! Tente novamente!!!')


def Jogar():
    MostrarRegras()

    palavra_da_vez = random.choice(lista_palavras)

    letras_tentadas = []
    n_tentativas = 0
    n_tentativas_erradas = 0

    FormatoPalavraEscondida(palavra_da_vez)

    while True:

    # === Faz a pergunta e faz o tratamento de caso cometa algum erro ===

        letra_digitada = LerLetra()



    # === Trata o erro de caso repetir a mesma letra como resposta ===

        if LetraRepetida(letra_digitada, letras_tentadas):
            print(
                "\nErro! Você infringiu a regra:\n"
                f"{regras[2]}\n"
                "Tente novamente!\n"
            )
            continue



    # === Acrescenta a letra digitada na lista de letra corretas ===

        letras_tentadas.append(letra_digitada)



    # === Acrescenta o número de tentativas feitas até o momento ===

        n_tentativas += 1



    # === Verifica se a letra digitada não esta na palavra ===

        if NormalizarAcentos(letra_digitada) not in NormalizarAcentos(palavra_da_vez):
            n_tentativas_erradas += 1



    # === Monta a palavra para mostrar ao jogador após a sua jogada ===

        palavra_atual = MontarPalavraAtual(
            palavra_da_vez,
            letras_tentadas
        )



    # === Informações mostradas ao jogador após realizar a jogada ===

        print(f'\nPalavra secreta: {palavra_atual}')
        print(f'Tentativas: {n_tentativas}')
        MostrarCorpo(n_tentativas_erradas)



    # === Mensagem final caso o jogador perca a partida ===

        if Perdeu(n_tentativas_erradas, 4, palavra_da_vez):
            break



    # === Mensagem final caso o jogador ganhe a partida ===

        if Venceu(palavra_atual, palavra_da_vez):
            print('\nPARABÉNS!!! VOCÊ GANHOU!!!')
            print(f'A palavra secreta era: {palavra_da_vez}')
            print(f'Você teve um total de {n_tentativas} tentativas')
            MostrarCorpo(n_tentativas_erradas)

            break



# -----------------------------------------------------------------------------
#            === Junção de todas as funções para o jogo rodar ===
# -----------------------------------------------------------------------------

def main():

# === Executa o jogo ===

    while True:
        Jogar()


# === Executa a função onde da opção de sair ou continuar jogando ===
    
        if not ContinuarOuPararJogo():
            break



# -----------------------------------------------------------------------------
#                     === Execução do jogo completo ===
# -----------------------------------------------------------------------------

main()