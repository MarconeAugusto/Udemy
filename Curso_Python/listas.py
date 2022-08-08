"""
Listas (List)

Funcionam como vetores ou matrizes dinâmicos e podem armazenar qualquer tipo de dados.
Dinâmico -> tamanho e tipo de dados
listas são representadas por []
"""

print(type([]))

lista1 = [1, 99, 4, 27, 15, 22]
lista2 = ["a", "d", "j", " ", "M"]
lista3 = []
lista4 = list(range(11)) # list gera uma lista
lista5 = list("Marcone Augusto")

# Checar se determinado valor está na lista
num = 8
if num in lista4:
    print(f"Encontrado o número {num}")
else:
    print(f"Não encontrado o número {num}")

# Ordenar os valores de uma lista
lista1.sort()
print(lista1)

# Contar o número de ocorrencias de um valor em uma lista
oco = lista5.count("o")
print(f"Foram encontradas {oco} vezes")

# Adicionar elementos em uma lista "append("valor") ou extend("valor_iterável")"
print(lista1)
lista1.append(42)
print(lista1)
lista1.append([11, 21, 31])     #Adiciona uma sublista dentro da lista
lista1.extend([10, 20, 30])     #adiciona os elementos 1 a 1

# Inserrir um novo valor na lista sem substituir o valor inicial
lista1.insert(2, "Novo valor")

# Juntar duas listas com soma ou extend
lista6 = lista4 + lista2
print(f"lista6: {lista6}")
lista6 = []
lista6.extend(lista4)
lista6.extend(lista2)
print(f"lista6: {lista6}")

# Inverter o sentido das listas com reverse ou slice
lista2.reverse()
print(f"Lista 2 reversa: {lista2}")
print(f"Lista 4 reversa: {lista4[::-1]}")

# Copiar uma lista
lista7 = lista5.copy()
print(f"Cópia da lista 5: {lista7}")

# Obter a quantidade de elementos em uma lista
qtd_elementos = len(lista7)
print(f"O tamnaho é: {qtd_elementos}")

# Remover o último elemento pop(), além disso a função retorna o elemto removido
print(f"Lista 7, antes de remover: {lista7}")
elemento_removido = lista7.pop()
print(f"Lista 7, {lista7}, com o seguinte elemento removido: {elemento_removido}")

# Remover um elemento pelo índice
print(f"Lista 7, antes de remover: {lista7}")
elemento_removido = lista7.pop(1)
print(f"Lista 7, {lista7}, com o seguinte elemento removido: {elemento_removido}")

# Zerar uma lista
lista8 = lista1.copy()
print(f"Lista 8, antes de remover: {lista8}")
lista8.clear()
print(f"Lista 8 zerada: {lista8}")

# Repetir elementos em uma lista
lista8 = [1, 2, 3]
print(f"Lista 8: {lista8}")
lista8 *= 3      # ou lista8 = lista8 * 3
print(f"Lista 8: {lista8}")

# Converter string para lista split(), por padrão o argumento do split é " "
frase = "Curso de programação básica em python"
print(f"Frase: {frase}")
frase_lista = frase.split()
print(f"Lista com a frase: {frase_lista}")
frase = "Curso,de,programação,básica,em,python"
print(f"Frase: {frase}")
frase_lista = frase.split(",")  #Passando um argumento no split
print(f"Lista com a frase: {frase_lista}")

# Transformar lista em string " ".join(), com essa função adicionamos um espaço em branco a cada elemnto da lista, retornando uma string
frase_lista = ['Curso', 'de', 'programação', 'básica', 'em', 'python']
frase = " ".join(frase_lista)
print(f"Frase: {frase}")

# Colocar qualquer tipo de dado em uma mesma lista
lista9 = [1, 2.35, True, [1, 2, 3], False, "TESTE", "q"]
print(f"Lista 9: {lista9}")
print(type(lista9))

# Iterando sobre listas
# para uma lista de str a soma gera uma palavra, ou para uma lista de numeros eles serão somados, para isso, deve-se alterar o tipo da variável soma para: soma = 0
soma = ""
for elemento in lista2:
    print(elemento)
    soma += elemento
print(soma)

carrinho = []
produto = ""
while produto != "sair":
    produto = input("Adicione um produto na lista de compras ou digite sair: \n")
    if produto == "sair":
        break
    else:
        carrinho.append(produto)
for produto in carrinho:
    print(produto, end=", ")

# utilizando variáveis em listas
numeros = [1, 2, 3]
n1 = 1
n2 = 2
n3 = 3
numeros = [n1, n2, n3]

# Acessando os elementos pelo índice
#         0/-4    1/-3       2/-2     3/-1
cores = ["azul", "verde", "amarelo", "azul"]
print(f"Cor: {cores[1]}")
print(f"Cor: {cores[-3]}")    # A lista se comporta como um cículo fechado, podendo acessar os elentos de forma reversa


# iteração em uma lista
for cor in cores:
    print(cor)
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

# For obtendo o indice e o elemento
print("\n")
for indice, cor in enumerate(cores):
    print(indice, cor)

# Encontrar o índice de um elemento, apenas a primeira aparição
numeros = list(range(10))
numeros.append(8)   # Adicionando outro 8 a lista
for indice, elemento in enumerate(numeros):
    if elemento == 8:
        print(f"Posiçaõ: {indice}")
    else:
        pass
print(f"Posição: {numeros.index(8)}")   # Se não possuir o valor passado como parâmetro gera ERRO
print(f"Posição: {numeros.index(8, 9)}")   # Buscando pelo 8 à partir do índice 9
print(f"Posição: {numeros.index(8, 3, 9)}")   # Buscando pelo 8 entre os índices 3 e 9

# Slice em listas
lista = list(range(10))
print(f"Slice de início: {lista[3:]}")                  # começa em 3 até o fim
print(f"Slice de fim: {lista[:3]}")                     # começa em 0 até 3 - 1
print(f"Slice de início e fim: {lista[3:8]}")           # começa em 3 até 8 - 1
print(f"Slice de início, fim e passo: {lista[3:8:2]}")  # começa em 3 até 8 - 1 de 2 em 2
print(f"Slice de passo: {lista[::2]}")                  # começa em 0 até o fim de 2 em 2
print(f"Slice de passo: {lista[::-2]}")                 # começa do fim ao início de 2 em 2

# Soma, Valor máximo, Valor Mínimo(****para valores inteiros ou reais) e Tamanho.
lista = list(range(10))
print(sum(lista))   #soma
print(max(lista))   #máximo
print(min(lista))   #minimo
print(len(lista))   #tamanho

# Transformar lista em tupla
print(f"Lista: {lista}, Tipo: {type(lista)}")
tupla = tuple(lista)
print(f"Tupla: {tupla}, Tipo: {type(tupla)}")

# Desempacotamento de listas
lista = [1, 2, 3]
n1, n2, n3 = lista      # O número de elementos e variáveis para receber os valores deve ser igual
# n1, n2, n3, n4 = lista      # ERRO
# n1, n2 = lista      # ERRO
print(f"Desempatamento: {n1}, {n2} e {n3}")

# Copiando listas (Shallow copy e Deep Copy)
# Deep copy
print(f"Lista original: {lista}")
nova = lista.copy()         # Gera uma nova lista com os mesmos valores porem idependende da anterior (Deep Copy)
print(f"Lista .copy(): {nova}")
nova.append(4)
print(f"Lista original: {lista}")
print(f"Lista .copy(): {nova}")

# Shallow copy
print(f"Lista original: {lista}")
nova = lista                # Copia via atribuição, as alterações em qualquer lista interfere na outra
print(f"Nova = Lista: {nova}")
nova.append(4)
print(f"Lista original: {lista}")
print(f"Nova = Lista {nova}")
