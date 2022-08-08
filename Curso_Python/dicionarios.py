"""
Dicionários

Coleções do tipo chave/valor e são representados por chaves {}
    As chaves e valores podem ser de qualquer tipo, porém, as chaves devem ser únicas
"""
print(type({}))

# Criação de dicionários
# Forma 1
paises = {"br": "Brasil", "eua": "Estados Unidos", "py": "Paraguai"}
print(f"Dicionário de países: {paises}, do tipo {type(paises)}")
# Forma 2
paises = dict(br="Brasil", eua="Estados Unidos", py="Paraguay")
print(f"Dicionário de países: {paises}, do tipo {type(paises)}")


# Acessando elementos
# Forma 1 - Acessando via chave
print(paises["br"])     # Se a chave não existir gera um erro
# Forma 2 - Acessando via get (Recomendado)
pais = paises.get("py")        # Se a chave não existir retorna None, sem erro
if pais:
    print(f"País encontrado: {pais}")
else:
    print("Pais não encontrado")

pais = paises.get("pu", "Não encontrado")   # get() com retorno fixo, para objetos não encontrados
print(f"País encontrado: {pais}")


# Verificar se exite uma chave no dicionário
print("br" in paises)
print("RU" in paises)
print("Brasil" in paises)   # A busca é realizada apenas com a chave, não com o valor


# Pode ser utilizado com qualquer tipo de dados (int, float, string, boolean, lista, tupla, dicionário)
localidades = {(35.6895, 39.6917): "Escritório em Tókio", (36.6885, 40.6917): "Escritório em São Paulo",
               (40.6885, 55.6917): "Escritório em Roma"}
print(f"Dicionário de localidades: {localidades}, do tipo {type(localidades)}")


# Adicionar elementos a um dicionário .update()
receita = {"Jan": 100, "Fev": 200, "Mar": 300}
print(f"Dicionário de receita: {receita}, do tipo {type(receita)}")
# Forma 1
receita["Abr"] = 400
print(f"Dicionário de receita: {receita}, do tipo {type(receita)}")
# Forma 2
receita.update({"Mai": 500})
print(f"Dicionário de receita: {receita}, do tipo {type(receita)}")


# Atualizar dados em um dicionário
# Forma 1
receita["Abr"] = 450
# Forma 2
receita.update({"Mai": 550})
print(f"Dicionário de receita: {receita}, do tipo {type(receita)}")


# Remover dados de um dicionário
# Forma 1
ret = receita.pop("Mai")      # Diferentemente das listas, é obrigatório possuir uma chave no pop(chave), se não for encontrada retorna erro
ret = receita.pop("Mao", "Não Removido")    # Para evitar erro podemos definir um retorno padrão para quando a chave não é encontrada
print(f"Valor removido: {ret}")    # O valor removido é retornado pela função pop()
print(f"Dicionário de receita: {receita}, do tipo {type(receita)}")
# Forma 2
del receita["Jan"]          # Se a chave não existir retorna erro
print(f"Dicionário de receita: {receita}, do tipo {type(receita)}")

"""
Cenário de utilização - Compras
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;
"""
# 1 - Solução utilizando listas, teriámos que saber o índice de cada informação do produto
carrinho = []
produto1 = ["livro", 1 , 25.00]
produto2 = ["livro 2", 1 , 35.00]
carrinho.append(produto1)
carrinho.append(produto2)
print(f"Carrinho de compras: {carrinho}, do tipo {type(carrinho)}")

# 2 - Solução utilizando tupla, teriámos que saber o índice de cada informação do produto
produto1 = ("livro", 1 , 25.00)
produto2 = ("livro 2", 1 , 35.00)
carrinho = produto1 + produto2
print(f"Carrinho de compras: {carrinho}, do tipo {type(carrinho)}")

# 3 - Solução utilizando Dicionário
carrinho = []
produto1 = {"Nome": "livro", "qtd": 1, "preco": 25.00}
produto2 = {"Nome": "livro 2", "qtd": 1, "preco": 35.00}
carrinho.append(produto1)
carrinho.append(produto2)
print(f"Carrinho de compras: {carrinho}, do tipo {type(carrinho)}")


# Métodos de dicionários
d = dict(a=1, b=2, c=3)
print(f"Dicionário: {d}, do tipo {type(d)}")

# Limpar o dicionário
d.clear()
print(f"Dicionário: {d}, do tipo {type(d)}")

# Copiar um dicionário
# Forma 1 - Deep Copy (Após a cópia os dicionários permanecem distintos)
d = dict(a=1, b=2, c=3)
novo = d.copy()
print(f"Dicionário novo: {novo}, do tipo {type(novo)}")
novo["d"] = 4
print(f"Dicionário d: {d}, do tipo {type(d)}")
print(f"Dicionário novo: {novo}, do tipo {type(novo)}")
# Forma 2 - Shallow Copy (Após a cópia os dicionários continuam iguais, mesmo que sejam feitas alterações em apena um)
d = dict(a=1, b=2, c=3)
novo = d
print(f"Dicionário: {novo}, do tipo {type(novo)}")
novo.update({"d": 4})
print(f"Dicionário d: {d}, do tipo {type(d)}")
print(f"Dicionário novo: {novo}, do tipo {type(novo)}")

# Forma não usual para criar dicionário utilizando fromkeys(chave_iterável, valor)
#                 chave, valor
outro = {}.fromkeys("a", "b")
print(f"Dicionário outro: {outro}, do tipo {type(outro)}")
#                                  chaves,                    valor para todas as chaves
user = {}.fromkeys(["nome", "e-mail", "endereço", "telefone"], "desconhecido")
print(f"Dicionário outro: {user}, do tipo {type(user)}")
str_cada_letra = {}.fromkeys("Marcone", "teste") # Cada letra da str vira uma nova chave
print(f"Dicionário outro: {str_cada_letra}, do tipo {type(str_cada_letra)}")


# Iterar sobre dicionários
receita = {"Jan": 100, "Fev": 200, "Mar": 300}
for chave in receita:
    print(chave)
for chave in receita:
    print(receita[chave])
for chave in receita:
    print(f"Em {chave}  recebi: R${receita[chave]}")


# Obter todas as chaves do dicionário
print(receita.keys())
for chave in receita.keys():
    print(receita[chave])


# Obter todas os valores do dicionário
print(receita.values())
for valor in receita.values():
    print(valor)


# Desempacotar dicionário
for chave, valor in receita.items():
    print(f"Em {chave}  recebi: R${receita[chave]}")


# Soma, Valor máximo, Valor Mínimo e Tamanho
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
