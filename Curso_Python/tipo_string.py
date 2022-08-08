"""
Tipo string

Dados entre àspas simples, àspas duplas, àspas simples triplas e àspas duplas triplas
"""

nome = "Marcone"
print(nome)
print(type(nome))

nome = "Angelina \n Jolie"
# Outra forma de fazer a mesma coisa
nome = """Angelina
Jolie"""
print(nome)
print(type(nome))

nome = "Marcone Augusto"
print(nome.upper())
print(nome.lower())
print(nome.title())
print(nome.split()) # Cria uma lista de strings
print(nome[0:7])    # Slice de string - Pega apenas uma parte da string
print(nome[8:15])   # Slice de string - Pega apenas uma parte da string

# Inverter a string
# Começa do primeiro elemento e vai até o último elemento e inverte com o -1
print(nome[::-1])

# Substituir letras
print(nome.replace("o", "O"))

# Palíndromo
texto = "socorram me subino onibus em marrocos"
print(texto)
print(texto[::-1])