#comprimento de reta de triangulo: pode formar reta?

r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('É possível formar um triângulo.')
else:
    print('não é possível formar um triângulo.')
    quit(' ')

if r1 == r2 == r3:
    print('O triângulo é equilátero.')
elif r1 == r2 or r2 == r3 or r1 == r3:
    print('O triângulo é isósceles.')
else:
    print('O triângulo é escaleno.')


if r1 <= 0 or r2 <= 0 or r3 <= 0:
    print('Os lados devem ser maiores que zero.')
    quit(' ')