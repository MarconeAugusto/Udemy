"""
Escopo de Variáveis

1 - Variável Global
    São reconhecidas em todo o código

2 - Variável local
    São reconhecidas apenas na função declarada
"""

numero = 42     # Variável global
print(numero)

if numero < 10:
    novo = numero + 10  # Variável local "novo"
    print(novo)
