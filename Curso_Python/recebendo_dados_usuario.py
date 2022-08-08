"""
Recebendo dados do usuário

input() -> entrada sempre como string
"""

# Entrada de dados
# print("Qual é o seu nome?")
# nome = input()
nome = input("Qual é o seu nome?\n")

# Processamento

# Saída de dados
# Python 2.x
print("Seja bem-vindo(a) %s" % nome)
# Python 3.x
print("Seja bem-vindo(a) {0}".format(nome))
# Python 3.7
print(f"Seja bem-vindo(a) {nome}")


# print("Qual a sua idade?")
# idade = input()

idade = int(input("Qual é a sua idade?\n"))

# Python 2.x
print("O(A) %s tem %s anos" % (nome, idade))
# Python 3.x
print("O(A) {0} tem {1} anos".format(nome, idade))
# Python 3.7
print(f"O(A) {nome} tem {idade} anos")

print(f"O(A) {nome} nasceu em {2022 - int(idade)}")

