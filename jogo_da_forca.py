import os
import random
import unicodedata

os.system('cls' if os.name == 'nt' else 'clear')

# === Dicionários Utilizados para guardar as palavras em Português e Inglês ===
 
mensagens = {

    'pt' : {
        'bem_vindo' : '        SEJA BEM-VINDO AO JOGO DA FORCA',
        
        'regras_do_jogo' : 
        [
            'Regras do jogo:',
            ' 1. Digite apenas uma letra por vez.',
            ' 2. Só são aceitas letras como tentativa.',
            ' 3. Não são aceitas letras repetidas.',
            ' 4. A cada tentativa errada, uma parte do boneco é acrescentada à forca,'
            '\n (Caso forme o corpo completo, o jogador perde).\n'
        ],

        'digite_uma_letra' : 'Digite uma letra: ',
        'palavra_secreta' : 'Palavra Secreta: ',

        'mensagem_de_erro' : 
        [
            '\nErro! Você infringiu a regra:\n',
            'Tente novamente!\n'
        ],

        'partes_do_corpo' :
        [
            'Cabeça',
            'Tronco',
            'Braços',
            'Pernas'    
        ],

        'mensagens_corpo_na_forca' :
        [
            'Corpo na forca: ',
            'Corpo na forca: nenhuma parte formada\n'
        ],

        'informações_mostradas_ao_jogador' :
        [
            '\nPalavra secreta: ',
            'Tentativas: '
        ],

        'mensagens_perdeu' : 
        [
            'Número de erros excedidos, o corpo na forca foi completado!\n'
            'VOCÊ PERDEU!!!',
            'A palavra secreta era:'

        ],

        'mensagens_venceu' : 
        [
            '\nPARABÉNS!!! VOCÊ GANHOU!!!',
            'A palavra secreta era: ',
            'Você teve um total de',
            'tentativas'

        ],

        'continuar_ou_parar_jogo' : 
        [
            'Deseja continuar jogando (Sim/Não)? ',
            'Você saiu!!!',
            'Carregando novo jogo...\n',
            'Resposta inválida!!! Tente novamente!!!',
            'sim',
            'não',
            'nao'
        ]
    }, 

    
    'en' : {
        'bem_vindo' : '              WELCOME TO HANGMAN ',
        
        'regras_do_jogo' : 
        [
            'Game rules:',
            " 1. Enter only one letter at a time.",
            " 2. Only letters are accepted as guesses.",
            " 3. It's not allowed to enter repeated letters.",
            " 4. For each wrong attempt, a part of the body will be placed on the gallows"
            "\n (If the body is completed, the player loses).\n"
        ],

        'digite_uma_letra' : "Enter a letter: ",
        'palavra_secreta' : "Secret word: ",

        'mensagem_de_erro' :
        [
            '\nError! You broke a rule:\n',
            'Try Again!\n'
        ],

        'partes_do_corpo' :
        [
            'Head',
            'Torso',
            'Arms',
            'Legs'    
        ],

        'mensagens_corpo_na_forca' :
        [
            'Body on the gallows: ',
            'Body on the gallows: no part formed\n'
        ],

        'informações_mostradas_ao_jogador' :
        [
            '\nSecret Word: ',
            'Guesses: '
        ],

        'mensagens_perdeu' : 
        [
            'Number of errors exceeded, the body in the gallows is complet!\n'
            'YOU LOST!!!',
            'The secret word was: '
        ],

        'mensagens_venceu' : 
        [
            '\nCONGRATULATIONS!!! YOU WON!!!',
            'The secret word was: ',
            'You got on total',
            'guesses'
        ],

        'continuar_ou_parar_jogo' : 
        [
            "Do you want to keep playing?(Yes/No)? ",
            'You left!!!',
            "Loading new game...\n",
            'Invalid Answer!!! Try Again!!!',
            'yes',
            'no',
            'n'

        ]

    }
}


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

def Escolher_Idioma():
    while True:
        print(
            'Select the language:\n\n'
            '1 - Português(Brasil)\n'
            '2 - English\n')

        idioma = input('Enter your choice: ')

        if idioma == '1':
            return 'pt'
        elif idioma == '2':
            return 'en'
        else:
            print('Invalid Option!'
                '\nTry Again!')
            continue


def Mensagem_Inicial(idioma):
    print('===============================================')
    print(f"{mensagens[idioma]['bem_vindo']}")
    print('===============================================\n')

    
def Mostrar_Regras(idioma):
    for regra in mensagens[idioma]['regras_do_jogo']:
        print(regra)


def Formato_Palavra_Escondida(palavra, idioma):
    n_letras_secretas = ''

    for _ in palavra:
        n_letras_secretas += '_'

    print(f"{mensagens[idioma]['palavra_secreta']}{n_letras_secretas}")


def Ler_Letra(idioma):
    while True:
        letra = input(mensagens[idioma]['digite_uma_letra']).lower()

        print('------------------------------------------------')

        if len(letra) != 1:
            print(
                f"{mensagens[idioma]['mensagem_de_erro'][0]}"
                f"{mensagens[idioma]['regras_do_jogo'][1]}\n"
                f"{mensagens[idioma]['mensagem_de_erro'][1]}"
            )
            continue

        if not letra.isalpha():
            print(
                f"{mensagens[idioma]['mensagem_de_erro'][0]}"
                f"{mensagens[idioma]['regras_do_jogo'][2]}\n"
                f"{mensagens[idioma]['mensagem_de_erro'][1]}"
            )
            continue

        return letra


def Normalizar_Acentos(texto):
    texto = unicodedata.normalize('NFD', texto)

    texto = ''.join(
        caractere
        for caractere in texto
        if unicodedata.category(caractere) != 'Mn'
    )

    return texto


def Letra_Repetida(letra, letras_tentadas):
    letra_normalizada = Normalizar_Acentos(letra)

    for letra_tentada in letras_tentadas:
        if Normalizar_Acentos(letra_tentada) == letra_normalizada:
            return True

    return False


def Montar_Palavra_Atual(palavra, letras_tentadas):
    palavra_atual = ''

    for letra in palavra:

        letra_encontrada = False

        for letra_tentada in letras_tentadas:
            if Normalizar_Acentos(letra_tentada) == Normalizar_Acentos(letra):
                letra_encontrada = True
                break

        if letra_encontrada:
            palavra_atual += letra
        else:
            palavra_atual += '_'

    return palavra_atual


def Mostrar_Corpo(tentativas_erradas, idioma):
    partes_corpo = mensagens[idioma]['partes_do_corpo']

    corpo_formado = partes_corpo[:tentativas_erradas]

    if corpo_formado:
        print(f"{mensagens[idioma]['mensagens_corpo_na_forca'][0]}{', '.join(corpo_formado)}\n")
    else:
        print(f"{mensagens[idioma]['mensagens_corpo_na_forca'][1]}")


def Perdeu(tentativas_erradas, maximo_erros, palavra_revelada, idioma):
    if tentativas_erradas >= maximo_erros:
        print(f"{mensagens[idioma]['mensagens_perdeu'][0]}")
        print(f"{mensagens[idioma]['mensagens_perdeu'][1]}{palavra_revelada}")

        return True

    return False


def Venceu(palavra_atual, palavra_escondida):
    return palavra_atual == palavra_escondida


def Continuar_Ou_Parar_Jogo(idioma):
    while True:
        pergunta_de_saida = input(
            f"{mensagens[idioma]['continuar_ou_parar_jogo'][0]}"
        ).lower()

        if pergunta_de_saida == mensagens[idioma]['continuar_ou_parar_jogo'][5]\
        or pergunta_de_saida == mensagens[idioma]['continuar_ou_parar_jogo'][6]:
            print(f"{mensagens[idioma]['continuar_ou_parar_jogo'][1]}")
            return False

        elif pergunta_de_saida == mensagens[idioma]['continuar_ou_parar_jogo'][4]:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{mensagens[idioma]['continuar_ou_parar_jogo'][2]}")
            return True

        else:
            print(f"{mensagens[idioma]['continuar_ou_parar_jogo'][3]}")


def Jogar(idioma):
    Mensagem_Inicial(idioma)
    Mostrar_Regras(idioma)

    palavra_da_vez = random.choice(lista_palavras)

    letras_tentadas = []
    n_tentativas = 0
    n_tentativas_erradas = 0

    Formato_Palavra_Escondida(palavra_da_vez, idioma)

    while True:

    # === Faz a pergunta e faz o tratamento de caso cometa algum erro ===

        letra_digitada = Ler_Letra(idioma)



    # === Trata o erro de caso repetir a mesma letra como resposta ===

        if Letra_Repetida(letra_digitada, letras_tentadas):
            print(
                f"{mensagens[idioma]['mensagem_de_erro'][0]}"
                f"{mensagens[idioma]['regras_do_jogo'][3]}\n"
                f"{mensagens[idioma]['mensagem_de_erro'][1]}"
            )
            continue



    # === Acrescenta a letra digitada na lista de letra corretas ===

        letras_tentadas.append(letra_digitada)



    # === Acrescenta o número de tentativas feitas até o momento ===

        n_tentativas += 1



    # === Verifica se a letra digitada não esta na palavra ===

        if Normalizar_Acentos(letra_digitada) not in Normalizar_Acentos(palavra_da_vez):
            n_tentativas_erradas += 1



    # === Monta a palavra para mostrar ao jogador após a sua jogada ===

        palavra_atual = Montar_Palavra_Atual(
            palavra_da_vez,
            letras_tentadas
        )



    # === Informações mostradas ao jogador após realizar a jogada ===

        print(f"{mensagens[idioma]['informações_mostradas_ao_jogador'][0]}{palavra_atual}")
        print(f"{mensagens[idioma]['informações_mostradas_ao_jogador'][1]}{n_tentativas}")
        Mostrar_Corpo(n_tentativas_erradas, idioma)



    # === Mensagem final caso o jogador perca a partida ===

        if Perdeu(n_tentativas_erradas, 4, palavra_da_vez, idioma):
            break



    # === Mensagem final caso o jogador ganhe a partida ===

        if Venceu(palavra_atual, palavra_da_vez):
            print(f"{mensagens[idioma]['mensagens_venceu'][0]}")
            print(f"{mensagens[idioma]['mensagens_venceu'][1]}{palavra_da_vez}")
            print(
                    f"{mensagens[idioma]['mensagens_venceu'][2]}",
                    f"{n_tentativas}",
                    f"{mensagens[idioma]['mensagens_venceu'][3]}"
                )
            
            Mostrar_Corpo(n_tentativas_erradas, idioma)

            break



# -----------------------------------------------------------------------------
#            === Junção de todas as funções para o jogo rodar ===
# -----------------------------------------------------------------------------

def main():

# === Executa o jogo ===

    idioma = Escolher_Idioma()
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        Jogar(idioma)


# === Executa a função onde da opção de sair ou continuar jogando ===
    
        if not Continuar_Ou_Parar_Jogo(idioma):
            break



# -----------------------------------------------------------------------------
#                     === Execução do jogo completo ===
# -----------------------------------------------------------------------------

main()