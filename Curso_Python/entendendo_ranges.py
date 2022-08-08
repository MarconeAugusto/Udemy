"""
Ranges
- Conhecer o for para entender o range.
- O range proporciona uma melhor utilização para o for.

Range -> gerar sequências numéricas

# Forma 1 -> range(valor de parada) valor de parada não inclusivo
# Forma 2 -> range(valor_inicio, valor_parada), valor de parada não inclusivo
# Forma 3 -> range(valor_inicio, valor_parada, passo), valor de parada não inclusivo
# Forma 4 -> range(valor_inicio, valor_parada, decremento), valor de parada não inclusivo
"""

# Forma 1
print("\nrange(valor de parada)")
for i in range(3):
    print(i)

# Forma 2
print("\nrange(valor_inicio, valor_parada)")
for i in range(10, 15):
    print(i)

# Forma 3
print("\nrange(valor_inicio, valor_parada, passo)")
for i in range(100, 110, 2):
    print(i)

# Forma 4
print("\nrange(valor_inicio, valor_parada, decremento)")
for i in range(100, 90, -2):
    print(i)