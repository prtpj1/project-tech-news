import requests
import time
from parsel import Selector


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
    selector = Selector(html_content)

    news = {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css(".entry-title::text").get().rstrip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css(".author > a::text").get(),
        "comments_count": len(selector.css(".comment-list li").getall()) or 0,
        "summary": selector.xpath("string(//p)").get().rstrip(),
        "tags": selector.css(".post-tags a::text").getall(),
        "category": selector.css(".category-style > span.label::text").get(),
    }

    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
