"""
Estruturas condicionais

if (Se), else (Senão) e elif (Senão se)

Deve ter apenas um if e um else, e quantos elif forem necessários
"""

idade = 20

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Tem 18 anos")
elif idade == 26:
    print("Tem 26 anos")
else:
    print("Maior de idade")
