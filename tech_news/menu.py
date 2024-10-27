import sys
import os
from tech_news.scraper import get_tech_news

from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
    search_by_tag,
)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input(
        (
            "\nPressione ENTER para limpar o terminal "
            "e voltar para o menu de opções."
        )
    )


def analyzer_menu():
    while True:
        print("Selecione uma das opções a seguir:")
        print(" 0 - Popular o banco com noticias ➡️")
        print(" 1 - Buscar noticias por titulo ➡️")
        print(" 2 - Buscar noticias por data ➡️")
        print(" 3 - Buscar noticias por tag ➡️")
        print(" 4 - Buscar noticias por categoria ➡️")
        print(" 5 - Listar top 5 noticias ➡️")
        print(" 6 - Listar top 5 categorias ➡️")
        print(" 7 - Sair")

        option = input("Digite a opção desejada: ")
        try:
            match option:
                case "0":
                    print("Digite quantas noticias serão buscadas:")
                    num_news = int(input())
                    get_tech_news(num_news)
                    print(f"Banco populado com {num_news} noticias.")
                case "1":
                    title = input("Digite o titulo: ")
                    result = search_by_title(title)
                    print(result)
                case "2":
                    date = input("Digite a data no formato dd/mm/yyyy: ")
                    result = search_by_date(date)
                    print(result)
                case "3":
                    tag = input("Digite a tag: ")
                    result = search_by_tag(tag)
                    print(result)
                case "4":
                    category = input("Digite a categoria: ")
                    result = search_by_category(category)
                    print(result)
                case "5":
                    print("Não implementado ainda.")
                case "6":
                    print("Não implementado ainda.")
                case "7":
                    print("Saindo do programa...")
                    sys.exit()
                case _:
                    print("Opção inválida", file=sys.stderr)
        except Exception as error:
            print(f"An error occurred:{error}", file=sys.stderr)

        pause()
        clear_screen()
