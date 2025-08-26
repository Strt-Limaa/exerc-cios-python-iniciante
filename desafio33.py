#maior e menor número
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite o último número: '))

#Definindo o maior
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

#Definindo o menor
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print(f'O maior número é {maior}.')
print(f'O menor número é {menor}.')



