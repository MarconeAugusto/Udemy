"""
Loop For

Loop -> estrutura de repetição

for item in interavel:
    //execução do loop

range(valor_inicial, valor_final) OBS.: o valor final é não inclusivo
"""

nome = "Marcone Augusto"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

# Exemplo de for string
for letra in nome:
    print(letra)

# Exemplo de for lista
for numero in lista:
    print(numero)

# Exemplo de for range
for n in numeros:
    print(n)

# Iteração em indices
"""
enumerate is useful for obtaining an indexed list:
 |      (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
"""
for indice, letra in enumerate(nome):
    print(indice, " ", letra)

print("\n")

for valor in enumerate(nome):
    print(valor)


qtd = int(input("Qantas vezes o loop deve rodar?\n"))

for n in range(1, qtd+1):
    print(n)

qtd = int(input("Qantas vezes o loop deve rodar?\n"))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f"Informe o valor {n} de {qtd}: \n"))
    soma += num
print(f"O valor da soma é: {soma}")


# Exemplo de for string com o print na mesma linha, mudando o parâmetro "end"
for letra in nome:
    print(letra, end=" ")

"""
Emoji no python
"""
# Original U+1F60D
# Modificado U0001F60D
for _ in range(3):      # Utiliza o "_" quando não precisamos da variável de iteração do loop
    for num in range(1, 11):
        print(f"\U0001F60D"*num)

