#programa irá ler o nome da cidade e dizer se começa com "São" ou não

cidade = (input('\nDigite o nome da sua cidade:'))
cidade = cidade.title() # deixar as iniciais maiusculas pra padronizar
cidade = cidade.strip() # excluir linhas denecessárias
cidade = cidade.split()

if "São" in cidade[0]:
    print('Sua cidade começa com a palavra "São"')
else:
    print('Sua cidade não começa com a palavra "São".')

# if e in pra ver se o "São" ta na primeira lista (0)
# se tiver ele diz que tem, se não diz que não tem.

