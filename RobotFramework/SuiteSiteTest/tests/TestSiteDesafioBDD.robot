*** Settings ***
Resource         ../resources/Resource.robot
Test Setup       Abrir navegador
Test Teardown    Fechar navegador
### Setup: roda a keyord antes da suite ou teste
### Teardown: roda a keyord depois da suite ou teste

*** Test Case ***
Caso de teste 01: Pesquisar produto existente
    Dado que estou na página home do site
    Quando eu pesquisar pelo produto "Blouse"
    Então o produto "Blouse" deve ser listado na página de resultado da busca

Caso de teste 02: Pesquisar produto não existente
    Dado que estou na página home do site
    Quando eu pesquisar pelo produto "produtoNãoExistente"
    Então a página deve exibir a mensagem "No results were found for your search "produtoNãoExistente""

Caso de teste 03: Listar produtos
    Dado que estou na página home do site
    Quando eu passar o mouse por cima da categoria "Women" no menu principal superior de categorias
    Quando eu clicar na sub categoria "Summer Dresses"
    Então uma página com os produtos da categoria selecionada deve ser exibida

Caso de teste 04: Adicionar produtos no carrinho
    Dado que estou na página home do site
    Quando eu pesquisar pelo produto "t-shirt"
    Quando eu clicar no botão "Add to cart" do produto
    Então eu clico no botão "Proceed to checkout"

*** Keywords ***
Dado que estou na página home do site
    Acessar a pagina home do site

Quando eu pesquisar pelo produto "${PRODUTO}"
    Digitar o nome do produto "${PRODUTO}" no campo de pesquisa
    Clicar no botão Pesquisar

Então o produto "${PRODUTO}" deve ser listado na página de resultado da busca
    Conferir se o produto "${PRODUTO}" foi listado no site

Então a página deve exibir a mensagem "No results were found for your search "produtoNãoExistente""
    Conferir mensagem de erro "No results were found for your search "produtoNãoExistente""

Quando eu passar o mouse por cima da categoria "${CATEGORIA}" no menu principal superior de categorias
    Mause sobre a categoria "${CATEGORIA}"

Quando eu clicar na sub categoria "${CATEGORIA}"
    Clicar na sub categoria "${CATEGORIA}"

Então uma página com os produtos da categoria selecionada deve ser exibida
    Conferir categoria Summer Dresses

Quando eu clicar no botão "Add to cart" do produto
    Clicar no botão "Add to cart" do produto

Então eu clico no botão "Proceed to checkout"
## Corrigir a expectativa nos casos 3 e 4
