n1 = float(input('Me diga sua primeira nota:'))
n2 = float(input('Me diga sua segunda nota:'))
m = (n1+n2)/2
m = min((m,10)) #limitador da média da media em 10
print(f'Sua média é {m:.1f}')

if m >= 7:
    print('Parabéns! Você está aprovado neste ciclo.')
else:
    print('É uma pena... Você reprovou neste ciclo.')