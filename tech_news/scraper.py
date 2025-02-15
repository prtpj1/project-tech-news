import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
        "url": selector.css("link[rel=canonical]::attr(href)").get() or "",
        "title": (selector.css(".entry-title a::text").get() or "").rstrip(),
        "timestamp": selector.css("li.meta-date::text").get() or "",
        "writer": selector.css(".author > a::text").get() or "",
        "comments_count": len(selector.css(".comment-list li").getall()) or 0,
        "summary": (selector.xpath("string(//p)").get() or "").rstrip(),
        "tags": selector.css(".post-tags a::text").getall() or [],
        "category": (
            selector.css(".category-style > span.label::text").get() or ""
        ),
    }

    return news


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    news = []

    while len(news) < amount:
        html_content = fetch(url)
        links_news_on_page = scrape_novidades(html_content)

        for link in links_news_on_page:
            if len(news) == amount:
                break
            news.append(scrape_noticia(fetch(link)))
        url = scrape_next_page_link(html_content)

    create_news(news)
    return news
