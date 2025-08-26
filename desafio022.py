#mexendo com texto em python
nome = str(input('Digite seu nome inteiro:')).strip().title()

print('=' * 45)

print(f'seu nome com todas as letras maiusculas é\n' ,nome.upper().strip())
print('=' * 45)

print(f'seu nome tem {len(nome) - nome.count(' ')} letras')
print('=' * 45)

nome = nome.split()
print(f'você tem {len(nome[0])} letras no primeiro nome, {nome[0]}')
#print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
#isso é o comando find que vai até o primeiro caracter que a gente pediu e conta por quantos passou
print('=' * 45)
#outra coisa impostante ta no minuto 7:35 da aula de exercicios 22 do guanabara