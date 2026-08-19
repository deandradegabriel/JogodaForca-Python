import os
import random
import unicodedata 

os.system('cls')

print('===============================================')
print('        SEJA BEM-VINDO AO JOGO DA FORCA')
print('===============================================\n')


regras = [' 1. Digite apenas uma letra por vez.', 
          ' 2. Só é apenas aceito letras como tentativa.',
          ' 3. A cada tentativa errada, uma parte do boneco é acrescentada a forca.\n',
          '(Caso forme o corpo completo, o jogador perde.)',
        ]

lista_palavras = ['python',
                    'palavra',
                    'escolha',
                    'computador',
                    'trabalho'
                ]


letra_correta = ''
n_letras_secretas = ''
palavra_da_vez = random.choice(lista_palavras)
n_tentativas = 0
n_tentativas_erradas = 0
saidaOUentrada = 0

print(f'Regras do jogo: ')
for regra in range(3):
    print(regras[regra])


for _ in palavra_da_vez:
    if _ not in n_letras_secretas:
        n_letras_secretas += '_'

print(f'\nPalavra secreta: {n_letras_secretas}')

# -----------------------------------------------------------------------------

while True:

    palavra_atual = ''
    n_tentativas += 1

    letra_digitada = input('Digite uma letra: ').lower()
    print('------------------------------------------------')

# Erros
    
    if len(letra_digitada) > 1:
        print("\nErro! Você infringiu a regra:\n"
        f"{regras[0]}\n"
        " Tente novamente!\n")
        continue

    elif type(letra_digitada) != str:
        print("\nErro! Você infringiu a regra:\n"
        f"{regras[1]}\n"
        "Tente novamente!\n")
        continue
   

# Processamento da jogada

    if letra_digitada in palavra_da_vez:
        letra_correta += letra_digitada
    else:
        n_tentativas_erradas += 1

    for tentativa_atual in palavra_da_vez:
        if tentativa_atual in letra_correta:
            palavra_atual += tentativa_atual
        else:
            palavra_atual += '_'

    print(f'\nPalavra secreta: {palavra_atual}')

    if n_tentativas_erradas == 4:
        break

    

# Mensagem final

    if palavra_atual == palavra_da_vez:
        print('PARABÉNS!!! VOCÊ GANHOU!!!')
        print(f'A palavra secreta era {palavra_da_vez}')
        print(f'Você teve um total de {n_tentativas} tentativas\n')

# Saída ou continuação do jogo
        
        while True:
            pergunta_de_saida = input('Deseja continuar jogando (Sim/Não)? ').lower()
            if pergunta_de_saida == 'sim':
                print('Você saiu!!!')
                saidaOUentrada = 0
                break
            elif pergunta_de_saida == 'não':
                print('Carregando Novamente o Jogo...')
                saidaOUentrada = 1
                break
            else:
                print('Resposta inválida!!! Tente novamente!!!')
                continue

    if saidaOUentrada == 1:
        continue
    elif saidaOUentrada == 0:
        break