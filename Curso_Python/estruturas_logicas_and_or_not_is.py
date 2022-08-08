"""
Estruturas Lógicas and (e), or (ou), not (não), is (é)

Operadores unários
    not
Operadores binários
    or, and, is

Funcionamento
    and -> ambos precisam ser True
    or -> um ou outro precisa ser True
    not -> inverte o valor
"""

ativo = True
logado = True

if ativo and logado:
    print("Bem-vindo!")
else:
    print("Ative sua conta, cheque o seu e-mail")

if not ativo:
    print("Ative sua conta, cheque o seu e-mail")
else:
    print("Bem-vindo!")

if ativo is False:
    print("Ative sua conta, cheque o seu e-mail")
else:
    print("Bem-vindo!")

#ativo é True?
print(ativo is True)

nome = "Marcone"
print(nome == "marcone")
print(nome == "Marcone")
