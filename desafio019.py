import random
#escolher um aluno aleatório para apagar o quadro
aluno1 = str(input('digite o nome do aluno:'))
aluno2 = str(input('digite o nome do aluno:'))
aluno3 = str(input('digite o nome do aluno:'))
aluno4 = str(input('digite o nome do aluno:'))

if not aluno1 or not aluno2 or not aluno3 or not aluno4:
    print('erro')
    exit(' ')
nomesort = random.choice([aluno1, aluno2, aluno3, aluno4])
print("o aluno escolido foi {}".format(nomesort))

#Estranhei o uso de parenteses
#e colchetes nessa ordem, porque sem eles o codigo não dá certo#
