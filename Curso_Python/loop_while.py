"""
Loop while

while expressão_booleana:
    // execução do loop

O bloco é repetido enquanto a expressão booleana for verdadeira
OBS.: Atenção ao loop infinito
"""

num = 1
while num < 10:
    print(num)
    num += 1

resposta = " "
while resposta != "sim":
    resposta = input("Já acabou? \n")
