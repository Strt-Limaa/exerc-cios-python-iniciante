#primeiro e último nome
nome = input("Digite seu nome completo:").title().split() #não prescisa de .strip porque o split ja elimina espaços
print(f'Seu primeiro nome é {nome[0]} e seu último nome é {nome[-1]}.')

