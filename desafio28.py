import random
#jogo para acertar um número aleatrório entre 1 e 5
num = random.randint(1,5)

resposta = int(input('Tente acertar o número de 1 a 5 que eu pensei:'))

if resposta == num:
    print(f'Parabéns, resposta certa!\nO número escolhido foi o {num}.')
else:
    print(f'Resposta errada!\nO número escolhido foi o {num}.')

