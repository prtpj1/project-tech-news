import requests
import time
from parsel import Selector

"""
html = fetch("https://blog.betrybe.com/")
scrape_next_page_link(html)
"""


# Requisito 1
def fetch(url):
    try:
        fake = {"user-agent": "Fake user-agent"}
        response = requests.get(url, headers=fake)
        time.sleep(1)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    news = []
    for new in selector.css(".entry-preview"):
        url = new.css("a::attr(href)").get()
        news.append(url)
    return news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css("a.next.page-numbers::attr(href)").get()

    return next_page


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
