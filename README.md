# Projeto Tech News

Projeto feito como critério avaliativo na escola de programação Trybe.

Foi utilizada a linguagem de programação Python.

O objetivo do projeto foi consolidar o conhecimento em raspagem de dados de páginas web utilizando a linguagem Python, através dos pacotes requests
e parsel. Após a extração, os dados são armazenados em formatos de documentos no banco de dados MongoDb utilizando o pacote pymongo. Por se tratar de
raspagem de dados, o código pode não extrair os dados como esperado, por depender da estruturação da página HTML no momento da sua criação e execução.

## Instruções para reproduzir o projeto

#### Pré Requisitos

Possuir Python instalado

Possuir MongoDb instalado e iniciado

---

1. Clone o repositório
  * `git@github.com:Kevin-Ol/project-tech-news.git`.
  * Entre na pasta do repositório que você acabou de clonar:
    * `cd project-tech-news`

2. Inicie e ative um ambiente virtual
  * `python3 -m venv .venv && source .venv/bin/activate`

3. Instale as dependências
  * `python3 -m pip install -r dev-requirements.txt`

obs: caso haja algum problema na instalação do pacote wheel, reinstale-o com o comando
  * `python3 -m pip install wheel`
---

Os requisitos desenvolvidos no projeto são:

`tech_news/scraper.py`

- Função `fetch`: possui como parâmetro uma url e é responsável por retornar o corpo HTML correspondente da requisição;

- Função `scrape_novidades`: possui como parâmetro um o corpo HTML e é responsável por retornar uma lista com a url dos links das notícias listadas;

- Função `scrape_next_page_link`: possui como parâmetro um o corpo HTML e é responsável por retornar a url do link para a próxima página de notícias;

- Função `scrape_noticia`: possui como parâmetro um o corpo HTML e é responsável por gerar um dicionário contendo os dados principais de uma notícia;

- Função `get_tech_news`: possui como parâmetro um número e é responsável por gerar uma lista de notícias com tamanho igual ao informado, bem como salvar
essas notícias no banco de dados, utilizando as funções criadas anteriormente;

`tech_news/analyzer/search_engine.py`

- Função `search_by_title`: possui como parâmetro uma string e é responsável por retornar uma lista de tuplas contendo o título e o link de notícias 
armazenadas no banco de dados contendo a string informada em seu título;

- Função `search_by_date`: possui como parâmetro uma data no formato aaaa-mm-dd e é responsável por retornar uma lista de tuplas contendo o 
título e o link de notícias armazenadas no banco de dados correspondente à data informada;

- Função `search_by_source`: possui como parâmetro uma string e é responsável por retornar uma lista de tuplas contendo o título e o link de notícias 
armazenadas no banco de dados contendo a string informada na lista de fontes;

- Função `search_by_category`: possui como parâmetro uma string e é responsável por retornar uma lista de tuplas contendo o título e o link de notícias 
armazenadas no banco de dados contendo a string informada na lista de categorias;

`tech_news/analyzer/ratings.py`

- Função `top_5_news`: responsável por retornar uma lista de tuplas contendo o título e o link das 5 notícias mais populares armazenadas no banco de 
dados. A popularidade é medida de acordo com a soma de compartilhamentos e comentários da notícia;

- Função `top_5_categories`: responsável por retornar uma lista contendo as 5 categorias mais populares armazenadas no banco de dados. A popularidade 
é medida de acordo com a soma de compartilhamentos e comentários de notícias pertencentes à categoria;

`tech_news/menu.py`

- Função `analyzer_menu`: função interativa para ser executada no terminal, para que sejam realizadas as funcionalidades implementadas anteriormente.
Pode ser iniciada através do comando:

```bash
tech-news-analyzer
```
