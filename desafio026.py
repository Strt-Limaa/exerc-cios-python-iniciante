#mexendo com textos em python pt2
frase = input('Escreva algo:').strip().lower()

if "a" in frase:
    print(f'existem {frase.count("a")} letra/s "a" na frase')
if "ã" in frase:
    print(f'existem {frase.count("ã")} letra/s "ã" na frase')
if "á" in frase:
    print(f'existem {frase.count("á")} letra/s "á" na frase')

print("=" * 45)

if "a" in frase:
 print(f'a primeira letra "a" apareceu na posição {frase.find("a") +1}' ) #o +1 é para adicionar 1 posição, se não fica posição 0
 print(f'a última letra "a" aparece na posição {frase.rfind("a")}')
 print("=" * 45)

if "ã" in frase:
    print(f' a primeira letra "ã" aparece na posição {frase.find("ã") +1}')
    print(f' a última letra "ã" aparece na posição {frase.rfind("ã")}')
    print("=" * 45)

if "á" in frase:
    print(f' a primeira letra "á" aparece na posição {frase.find("á") +1}')
    print(f' a última letra "á" aparece na posição {frase.rfind("á")}') #o rfind vai começar a ver do fim
    print("=" * 45)
