import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


def analyzer_menu():
    messages = [
        "Digite quantas notícias serão buscadas:",
        "Digite o título:",
        "Digite a data no formato aaaa-mm-dd:",
        "Digite a fonte:",
        "Digite a categoria:",
    ]

    functionalities = [
        get_tech_news,
        search_by_title,
        search_by_date,
        search_by_source,
        search_by_category,
        top_5_news,
        top_5_categories,
    ]

    print(
        """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair."""
    )

    option_input = input()

    if not option_input.isdigit() or not 0 <= int(option_input) <= 7:
        return print("Opção inválida", file=sys.stderr)

    option_number = int(option_input)

    if option_number == 7:
        return print("Encerrando script")

    if option_number < 5:
        print(messages[option_number])
        parameter_input = input()
        if option_number == 0:
            parameter_input = int(parameter_input)
        return print(functionalities[option_number](parameter_input))

    return print(functionalities[option_number]())
