from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    searched_news = search_news({"title": {"$regex": title, "$options": "i"}})
    format_news = [(news["title"], news["url"]) for news in searched_news]

    return format_news


# Requisito 7
def search_by_date(date):
    try:
        format_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        searched_news = search_news({"timestamp": {"$eq": format_date}})
        format_news = [(news["title"], news["url"]) for news in searched_news]

        return format_news
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
