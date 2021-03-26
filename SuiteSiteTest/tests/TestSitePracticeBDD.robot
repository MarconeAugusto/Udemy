*** Settings ***
Resource          ../resources/Resource.robot


*** Test Case ***
Caso de teste 01: Pesquisar produto existente
  Dado que estou na página home do site
  Quando eu pesquisar pelo produto "Blouse"
  Então o produto "Blouse" deve ser listado na página de resultado da busca

Caso de teste 02: Pesquisar produto não existente
  Dado que estou na página home do site
  Quando eu pesquisar pelo produto "produtoNãoExistente"
  Então a página deve exibir a mensagem "No results were found for your search "produtoNãoExistente""

*** Keyords ***
