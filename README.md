# Data Scraper

Este é um aplicativo simples para obter e exibir informações sobre chamadas públicas da Finep (Financiadora de Estudos e Projetos) através do web scraping. O aplicativo usa as bibliotecas BeautifulSoup, requests, datetime, streamlit, unidecode e re para obter os dados do site da Finep, processá-los e exibi-los em uma interface gráfica usando Streamlit.

## Funcionalidades Principais

- **Atualizar Dados:** Ao clicar no botão "Atualizar Dados", o aplicativo obtém as informações mais recentes sobre chamadas públicas da Finep e exibe esses dados na tela.
- **Datas Identificadas:** O aplicativo também identifica as datas de publicação e prazo para envio de propostas de cada chamada pública e permite ao usuário selecionar uma data específica para envio de propostas.

## Bibliotecas Utilizadas

- **BeautifulSoup:** Para fazer o parsing do conteúdo HTML da página da Finep.
- **requests:** Para fazer a requisição HTTP à página da Finep e obter o conteúdo HTML.
- **datetime:** Para manipulação de datas.
- **streamlit:** Para criar a interface gráfica do aplicativo.
- **unidecode:** Para remover acentos e caracteres especiais do texto.
- **re:** Para fazer a busca por padrões de datas no texto.

## Funções Principais

- **fetch_data():** Esta função faz uma requisição GET à página da Finep, obtém o conteúdo HTML da página, faz o parsing do HTML usando BeautifulSoup e retorna uma lista com os nomes das chamadas públicas.
- **extract_dates(data):** Esta função recebe a lista de nomes das chamadas públicas e busca por padrões de datas dentro de cada nome. Ela retorna uma lista de tuplas contendo a data de publicação e o prazo para envio de propostas de cada chamada pública.
- **main():** Esta função é responsável por criar a interface gráfica do aplicativo usando Streamlit. Ela exibe um título, um botão para atualizar os dados, os dados atualizados e as datas identificadas. Também permite ao usuário selecionar uma data específica para envio de propostas.

## Uso

Para executar o aplicativo, basta rodar o código Python e acessar a URL fornecida pelo Streamlit no navegador. Ao clicar no botão "Atualizar Dados", o aplicativo irá buscar as informações mais recentes sobre chamadas públicas da Finep e exibi-las na tela.
