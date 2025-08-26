from math import hypot
#pitágoras
adj = float(input('Qual é o valor do cateto adjacente?'))
opo = float(input('Qual o valor do cateto oposto?'))
hipotenusa = hypot(adj, opo)
print('o comprimento da hipotenusa vale {:.1f}'.format(hipotenusa))