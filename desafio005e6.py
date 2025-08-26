#dizer o antecessor e o sucessor de um número e dizer o dobro, o triplo, e a raiz de outro
n1 = int(input('digite um número:'))
a = n1 - 1
p = n1 + 1
print("="*30)
print('o antecessor desse número é {}\ne o sucessor é {}'.format(a,p))
print("="*30)

n2 = int(input("digite um valor e eu mostrarei seu dobro, triplo \ne raiz quadrada"))

print("=" * 30)
print('o dobro de {} é {}, o seu triplo é {}\ne a sua raiz é {:.1f}'.format( n2, (n2 * 2), (n2 * 3) ,(n2 **1/2)))
print("=" * 30)