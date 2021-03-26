*** Settings ***
Resource         ../resources/Resource.robot
Test Setup       Abrir navegador
Test Teardown    Fechar navegador
### Setup: roda a keyord antes da suite ou teste
### Teardown: roda a keyord depois da suite ou teste


*** Test Case ***
Caso de Teste 01: Pesquisar produto existente
  Acessar a pagina home do site
  Digitar o nome do produto "Blouse" no campo de pesquisa
  Clicar no botão Pesquisar
  Conferir se o produto "Blouse" foi listado no site

Caso de Teste 02: Pesquisar produto não existente
  Acessar a pagina home do site
  Digitar o nome do produto "produtoNãoExistente" no campo de pesquisa
  Clicar no botão Pesquisar
  Conferir mensagem de erro "No results were found for your search "produtoNãoExistente""
