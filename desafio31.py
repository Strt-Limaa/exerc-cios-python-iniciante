#custo de viagem
dist = float(input('Qual é a distãncia da viagem em km/h?:'))
if dist < 200: #se a distancia for menor que 200
    pr = dist * 0.50
    print(f'A passagem custa {pr:.2f} reais.')
else:
    pr = dist * 0.45
    print(f'A passagem custa {pr:.2f} reais.')

