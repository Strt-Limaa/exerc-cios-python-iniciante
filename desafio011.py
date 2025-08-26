          ##### ÁREA DA PAREDE #####

l = input('Qual a altura da parede?:')

try:
    l = int(l)
except ValueError:
    l = float(l)
a = input('Qual a largura da parede?:')

try:
    a = int(a)
except ValueError:
    a = float(a)

area = l * a
quantidade = area / 2

print(f'Você precisará de {quantidade:.1f} Litros de tinta para pintar\nsua parede.')

