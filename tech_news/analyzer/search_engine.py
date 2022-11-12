from tech_news.database import search_news
from datetime import datetime


def format_news(searched_news):
    return [(news["title"], news["url"]) for news in searched_news]


# Requisito 6
def search_by_title(title):
    searched_news = search_news({"title": {"$regex": title, "$options": "i"}})

    return format_news(searched_news)


# Requisito 7
def search_by_date(date):
    try:
        format_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        searched_news = search_news({"timestamp": {"$eq": format_date}})

        return format_news(searched_news)

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    searched_news = search_news({"tags": {"$regex": tag, "$options": "i"}})

    return format_news(searched_news)


# Requisito 9
def search_by_category(category):
    searched_news = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )

    return format_news(searched_news)
