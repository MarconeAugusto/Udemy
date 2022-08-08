"""
Tuplas (tuple)

Tuplas são representadas por parênteses ()

As tuplas são imutáveis, ou seja, não muda. a cada operação uma nova tupla é criada
"""
# Tuplas
tupla_ex = (1, 2, 3, 4)
print(type(tupla_ex))
tupla_ex = 1, 2, 3, 4       # Pode ser criada sem os ()
print(type(tupla_ex))

# Tuplas com um elemento
tupla1 = (4)        # isso não é tupla, é apenas um int
print(f"tupla: {tupla1} do tipo {type(tupla1)}")
tupla1 = (4,)
print(f"tupla: {tupla1} do tipo {type(tupla1)}")
tupla1 = 4,
print(f"tupla: {tupla1} do tipo {type(tupla1)}")

# tuple através de um range
tupla1 = tuple(range(10))
print(f"tupla: {tupla1} do tipo {type(tupla1)}")

# Desempacotamento de tupla
tupla1 = ("Marcone", "Augusto")
p1, p2 = tupla1     # Atênção: a quantidade de elementos deve ser a mesma das variáveis
print(f"{p1} {p2}")

# Adição e remoção de elementos não existem nas tuplas (são imutáveis)

# Soma*, Valor máximo*, Valor mínimo* (para valores inteiros ou reais) e tamanho
tupla1 = tuple(range(10))
print(sum(tupla1))
print(max(tupla1))
print(min(tupla1))
print(len(tupla1))

# Concatenação de tuplas
tupla1 = tuple(range(5))
print(f"tupla: {tupla1} do tipo {type(tupla1)}")
tupla2 = tuple(range(5, 10))
print(f"tupla: {tupla2} do tipo {type(tupla1)}")
tupla3 = tupla1 + tupla2
print(f"tupla: {tupla3} do tipo {type(tupla3)}")

# Tuplas são imutáveis mas podem ser sobrescritas
tupla1 += tupla2
print(f"tupla: {tupla1} do tipo {type(tupla1)}")

# Verificar elemento na tupla
print(5 in tupla1)      # Expectativa True

# Iterando uma tupla
for n in tupla1:
    print(n, end=" ")
print("\n")
for i, n in enumerate(tupla1):
    print(f"Indice: {i}, valor: {n}", end=" ")
print("\n")

# Coletando elementos dentro de uma tupla
tupla2 = ("a", "b", "c", "a")
print(tupla2.count("a"))

# Dicas de utilização, utilizar quando não precisamos mofificar dados em uma coleção
meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro",
         "Novembro", "Dezembro")
print(f"tupla: {meses} do tipo {type(meses)}")

# Acesso a um determinado índice
print(f"Mês de {meses[11]}")

# Iterar com while
i = 0
while i < len(meses):
    print(meses[i])
    i += 1

# Verificar qual indice está o elemento
print(meses.index("Agosto"))    # caso a busca não exista retorna erro

# Slicing
print(meses[5:])
print(meses[:5])

# Copinado tuplas

tupla1 = (1, 2, 3)
print(f"tupla: {tupla1} do tipo {type(tupla1)}")
nova = tupla1
"""
Única forma de copiar uma tupla, sem acontecer o Shallow copy, ou seja, a tupla original não é  modificada quando a 
nova sofre alguma alteração
"""
print(f"tupla: {nova} do tipo {type(nova)}")
nova += (4, 5, 6)
print(f"tupla: {tupla1} do tipo {type(tupla1)}")
print(f"tupla: {nova} do tipo {type(nova)}")

# Por quê utilizar?
# Tuplas são mais rápidas do que listas para realizar operações
# Tuplas deixam o código mais seguro
