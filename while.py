# Jogo da Adivinhação que mede sua sorte ao encontrar o número secreto
from random import randint

tenta_denovo = True
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')

def inicia_jogo(integer):        
    sorte = randint(1,100)  # A dificuldade também é aleatória HAHAHA (sorte = 0:  GAME OVER)
    limite = 0
    secreto = randint(0, 9)
    escolhido = None        # Não pode ser número porque vai gastar chance do usuário ser pegar input
    print(f"""\033[3{randint(1, 7)}m
    -----------------------------------------------------------------------------------------
    |                  BEM-VINDO(A) AO JOGO DE ADIVINHAÇÃO PUNITIVO                         |
    -----------------------------------------------------------------------------------------
    """)                    # A cada vez que o jogo é executado, troca a cor dos caracteres
    while secreto != escolhido and sorte > limite:
        try:
            escolhido = input('Escolha um número de 0 a 9: ').lower()
            escolhido = integer(escolhido)      

        except ValueError: 
            print('\tSem um número, não tem graça!\nPode usar o cardinal como por extenso\n')
        
        else:
            if escolhido not in range(0, 10):
                print('\tO número precisa estar entre 0 e 9!\n')
            
        finally:
            if escolhido != secreto:
                sorte //= 2

    if secreto == escolhido:
        print(f'\n\t\tParabéns! Você descobriu o {tupla[secreto]} com {sorte}% de sorte\n')
                
    else:
        print('\t\t\tGAME OVER:\n\t\t\tNão descobriu o número secreto !!!\n')


def trata_bool(option):
    if option[0:1] == 'n':
        return False
    else: 
        return True


def trata_int(number):
    if number in tupla:
        number = tupla.index(number)

    return int(number)


while tenta_denovo:
    inicia_jogo(trata_int)
    tenta_denovo = trata_bool(input('Tentar outra vez? (s/n) ').lower())