# Importa a função randint do módulo random e a função sleep do módulo time
from random import randint
from time import sleep

# Gera um número aleatório entre 10 e 100
num_jogo = randint(10, 100)
# Inicializa variáveis globais
tentativas = 0
pontos = 0
erros = 0
chances = 0
palpite = None  # Inicializa a variável palpite como None

# Função que exibe as mensagens iniciais do jogo e chama a função escolha_nivel
def display():
    print('\033[1mPronto Para Começar?😁')
    sleep(2)
    print('Tente Acertar!')
    sleep(2)
    print('Você Começará Com 20 Tentativos Com 200 Pontos, 10 Tentativos Com 100 Pontos, 5 Tentativos Com 50 Pontos.!')
    sleep(2)
    print('A Cada Número Que Você Errar...')
    sleep(2)
    print('...Perderá 10 Pontos!')
    sleep(2)
    print('Boa Sorte!!!')
    sleep(2)
    print()
    print('Nivel De Dificuldade\n\033[32m1- Facil: 20 chances. \n\033[33m2- Médio: 10 chances. \n\033[31m3-Dificil: 5 chances.')
    print()
    escolha_nivel()  # Chama a função escolha_nivel

# Função que permite ao jogador escolher o nível de dificuldade
def escolha_nivel():
    global tentativas, pontos  # Indica que as variáveis tentativas e pontos são globais
    while True:
        try:
            escolha_do_nivel = int(input("\033[0mDigite nivel desejado: "))
            while escolha_do_nivel not in [1, 2, 3]:
                print('Nivel não existe!')
                escolha_do_nivel = int(input("Digite nivel desejado: "))
        except ValueError:
            print('Digite Apenas Os Valores Sugeridos.')
            continue
        print()
        if escolha_do_nivel == 1:
            tentativas += 20
            pontos += 200
        elif escolha_do_nivel == 2:
            tentativas += 10
            pontos += 100
        elif escolha_do_nivel == 3:
            tentativas += 5
            pontos += 50
        tentativa()  # Chama a função tentativa

# Função que realiza as tentativas do jogador
def tentativa():
    global pontos, erros, chances, palpite  # Indica que as variáveis são globais
    for x in range(tentativas):
        try:
            palpite = int(input("Qual seu palpite?: "))
            while palpite <= 10 or palpite >= 100:
                print('\033[1;31mO Palpite Tem Que Ser De \033[0m10 \033[1;31mA \033[0m100.')
                palpite = int(input('\033[0mQual seu palpite?: '))
        except ValueError:
            print('Digite apenas Números.')
            continue
        if palpite == num_jogo:
            print()
            print('Você Acertou! 🤘🙌🎆🎈🎇')
            print()
            pontos += 1000
            break
        elif palpite > num_jogo:
            print('Numero informado é maior!')
            print()
            pontos -= 5
            erros += 1
        elif palpite < num_jogo:
            print('Número informado é menor')
            print()
            pontos -= 5
            erros += 1
        chances += 1
        print(f'Você Usou {chances} chances De {tentativas} Tentavivas.')
        print()
    estatistica()  # Chama a função estatistica
    jogar_de_novo()  # Chama a função jogar_de_novo

# Função que pergunta ao jogador se deseja jogar novamente
def jogar_de_novo():
    global pontos, erros, chances, palpite  # Indica que as variáveis são globais
    print()
    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
    if jogar_novamente == 's':
        print()
        resetar_variaveis()
        escolha_nivel()
    else:
        print()
        print(15 * '=', 'FIM DE JOGO!', 15 * '=')
        print(15 * '=', 'ATÉ A PRÓXIMA 😉😉😉', 15 * '=')
        exit()

# Função que exibe as estatísticas do jogo
def estatistica():
    global palpite  # Indica que a variável palpite é global
    print(f'\033[32mO Número Era: \033[33m{num_jogo}')
    print()
    print(10 * '\033[32m=', '\033[0mSua Estatisticas De Jogo', 10 * '\033[32m=')  # Sua Estatisticas de jogo
    print()
    print(f'\033[0mVocê teve \033[31m{erros} \033[0m Erros Em \033[32m{tentativas}\033[0m Tentativas')
    print(f'\033[0mSua Pontuação Final Foi De: \033[32m{pontos}\033[0m')
    if palpite == num_jogo:
        print(f'Você Acertou Na Tentativa: \033[32m{chances}\033[0m')

# Função que reseta as variáveis globais
def resetar_variaveis():
    global tentativas, pontos, erros, chances, palpite  # Indica que as variáveis são globais
    tentativas = 0
    pontos = 0
    erros = 0
    chances = 0
    palpite = None

# Iniciar o jogo chamando a função display()
display()
