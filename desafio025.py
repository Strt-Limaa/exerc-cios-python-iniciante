#Tem "Silva" no seu nome?
nome = str(input('Digite seu nome completo:')).strip().title().split()
proibname = "Silva"
proibname.title()
if proibname in nome:
    print('Você tem "Silva" no nome')
else:
    print('Você não tem "Silva" no nome')
