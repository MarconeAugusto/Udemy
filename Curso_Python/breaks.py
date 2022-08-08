"""
Saindo de loops com o breack de maneira projetada
"""

# Exemplo for
for n in range(1,11):
    if n == 6:
        print("Saindo do loop")
        break
    else:
        print(n)

# Exemplo While
while True:
    command = input("Digite S para sair: \n")
    if command == "S":
        break