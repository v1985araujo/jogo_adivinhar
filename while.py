# Jogo da Adivinhação que mede sua sorte ao encontrar o número secreto
from random import randint

sorte = randint(1,100)          # A dificuldade também é aleatória HAHAHA
limite = 0
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
secreto = randint(0, 10)
escolhido = None
print("""
-----------------------------------------------------------------------------------------
|                  BEM-VINDO(A) AO JOGO DE ADIVINHAÇÃO PUNITIVO                         |
-----------------------------------------------------------------------------------------
""")


while secreto != escolhido and sorte > limite:
    try:
        escolhido = input('Escolha um número de 0 a 9: ').lower()
        if escolhido in tupla:
            escolhido = tupla.index(escolhido)

        escolhido = int(escolhido)

    except:
        sorte //= 2 # Lembram da parte punitiva?
        print(f'Sem um número, não tem graça!\nPode usar o cardinal como por extenso')
        
    
    if escolhido != secreto:
        sorte //= 2
        #print(f'Sua sorte caiu para {sorte}%')  # A idéia inicial era o jogador não saber quantas tentativas ele ainda tem


if secreto == escolhido:
    print(f"""
-----------------------------------------------------------------------------------------
|                         PÓDIO           DO          VENCEDOR                          |
-----------------------------------------------------------------------------------------
\n\t\tParabéns! Você descobriu o {tupla[secreto]} com {sorte}% de sorte\n""")
              
else:
    print("""
-----------------------------------------------------------------------------------------
|                               GAME               OVER                                 |
-----------------------------------------------------------------------------------------
\n\t\t\tNão descobriu o número secreto !!!\n""")