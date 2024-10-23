from tech_news.database import search_news
from datetime import datetime

# import json
from colorama import init, Fore

init(autoreset=True)


def format_news(searched_news):
    return [
        {"title": news["title"], "url": news["url"]} for news in searched_news
    ]


def colored_news(news_list):
    total_news = len(news_list)

    if not news_list:
        print(
            (
                f"{Fore.RED} Nenhuma noticia encontrada. "
                "Tente outra palavra ou data."
            )
        )

    for news in news_list:
        print(f"{Fore.WHITE}Title: {Fore.YELLOW}{news['title']}")
        print(f"{Fore.WHITE}URL: {Fore.LIGHTBLUE_EX}{news['url']}\n")

    print(
        (
            f"{Fore.WHITE}Total de noticias encontradas: "
            f"{Fore.LIGHTGREEN_EX}{total_news}"
        )
    )


# Requisito 6
def search_by_title(title):
    searched_news = search_news({"title": {"$regex": title, "$options": "i"}})
    formatted_news = format_news(searched_news)

    colored_news(formatted_news)
    return ""


# Requisito 7
def search_by_date(date):
    try:
        if "/" in date:
            day, month, year = date.split("/")
        elif "-" in date:
            day, month, year = date.split("-")
        else:
            raise ValueError("Formato de data inválido")

        iso_date = f"{year}-{month}-{day}"

        format_date = datetime.fromisoformat(iso_date).strftime("%d/%m/%Y")
        searched_news = search_news({"timestamp": {"$eq": format_date}})
        formatted_searched_news = format_news(searched_news)

        colored_news(formatted_searched_news)

        return ""

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    searched_news = search_news({"tags": {"$regex": tag, "$options": "i"}})
    formatted_news = format_news(searched_news)

    colored_news(formatted_news)

    return ""


# Requisito 9
def search_by_category(category):
    searched_news = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )
    formatted_news = format_news(searched_news)

    colored_news(formatted_news)

    return ""
