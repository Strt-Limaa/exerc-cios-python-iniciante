#programa de multa
vel = int(input('Digite a velociadedo carro em km/h:'))
if vel > 80:
    print('você foi multado por dirigir acima de\n80 km/h!')
else:
    print('você está livre.')

multa = (vel-80) *7 #a velocidade menos 80 (vel max) vezes 7 é o real por km (7)
if vel > 80:
    print(f'Multa: {multa} reais.')
