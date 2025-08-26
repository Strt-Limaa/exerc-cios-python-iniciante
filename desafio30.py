#número par ou ímpar?
number = int(input('Digite um número:'))

par = number % 2
if par == 0:
    print('Seu número é par.')
else:
    print('Seu número é ímpar.')
