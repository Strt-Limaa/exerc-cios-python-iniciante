#sálario da empresa
salario1 = float(input('Qual é o sálario do funcionário?:'))

if salario1 >= 1450:
    novo_salario = salario1 + (salario1 * 0.15)
    print(f'O novo sálario do funcionário é de {novo_salario:.2f}')

if salario1 <= 1450:
    novo_salario = salario1 + (salario1 * 0.20)
    print(f'O novo sálario do funcionário é de {novo_salario:.2f}')
