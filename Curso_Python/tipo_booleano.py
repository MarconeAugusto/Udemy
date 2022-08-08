"""
Tipo Booleano

True -> Verdadeiro
False -> Flaso

Sempre com a inicial em maiúsculo

"""

ativo = False
print(ativo)
print(type(ativo))

"""
Operações
"""

# Negação (not)
ativo = not ativo
print(ativo)

# Ou (or)
"""
Operação binário, ou um ou outro deve ser verdadeiro
"""
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# E (and)
"""
Operação binário, ambos os valores devem ser verdadeiros
"""
print(True and True)
print(True and False)
print(False and True)
print(False and False)