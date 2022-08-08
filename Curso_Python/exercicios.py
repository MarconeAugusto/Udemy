"""
    Exercício número 1
"""
# a
a = [1, 0, 5, -2, -7, 7]

# b
sum = 0
for i, v in enumerate(a):
    if i == 0 or i == 1 or i == 5:
        sum += v
print(sum)

# c
a[4] = 100
print(a)

# d
for v in a:
    print(v)

"""
    Exercício número 2
"""
lista_numeros = []
for i in range(6):
    numero = int(input("Digite o valor desejado: "))
    lista_numeros.append(numero)
print(lista_numeros)

"""
    Exercício número 3
"""

n_reais = [5, 7, 9, 2, 4, 3, 6, 1, 8, 10]
quadrado_n_reais = []
for n in n_reais:
    valor = n * n
    quadrado_n_reais.append(valor)
print(quadrado_n_reais)