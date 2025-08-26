import time

#programa que leia um número de 0 a 9999 e mostre
#na tela cada um dos digitos separados.

nume = str(input('Digite um número de 0 a 9999:'))

#só pra ficar legal
print(f'ANALISANDO {nume}...')
time.sleep(2) #espera 2 segundos

nume = nume.strip() #remove os espaços desnecessarios
if not nume.isnumeric():
    print('Erro')
    exit(' ') #Encerrando o programa

print('Seu número contém as seguintes informações:')
nume = nume.zfill(4) #completa com zeros à esquerda para ter sempre 4 dígitos
lista = len(nume)
print(f'Unidade: {nume[3]}')
print(f'Dezena: {nume[2]}')
print(f'Centena: {nume[1]}')
print(f'Milhar: {nume[0]}')
print('=' * 45)

#conteúdo importante sobre isso no exercicio 23 de python
