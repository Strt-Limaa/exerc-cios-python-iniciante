#é um ano bissexto ou não?
ano = int(input('digite o ano:'))

if ano % 4 == 0 or ano % 100 == 0 and ano % 400 == 0:
    print(f'{ano} é um ano bissexto.')
else:
    print(f'{ano} não é um ano bissexto.')
