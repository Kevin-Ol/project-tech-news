import requests
import time
from parsel import Selector
from tech_news.database import create_news


def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
    except requests.ReadTimeout:
        return None
    else:
        if response.status_code != 200:
            return None
        return response.text


def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news_links = selector.css(
        "main a.tec--card__title__link::attr(href)"
    ).getall()
    return news_links


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css("main a.tec--btn::attr(href)").get()
    return next_page


def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("#js-article-title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()

    writer = (
        selector.css(".tec--author__info p *::text").get()
        or selector.css(".tec--timestamp__item a::text").get()
    ).strip()

    shares_count = int(
        selector.css(".tec--toolbar__item::text").re_first(r"\d+") or 0
    )

    comments_count = int(
        selector.css("#js-comments-btn::text").re_first(r"\d+")
    )

    summary = selector.css(
        ".tec--article__body > p:first-child *::text"
    ).getall()
    summary = "".join(summary)

    sources = selector.css(
        ".tec--article__body-grid div:nth-last-child(2)  a.tec--badge::text"
    ).getall()
    for source in range(len(sources)):
        sources[source] = sources[source].strip()

    categories = selector.css("#js-categories a.tec--badge::text").getall()
    for category in range(len(categories)):
        categories[category] = categories[category].strip()

    return {
        "url": url,
        "title": title,
        "categories": categories,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "sources": sources,
        "summary": summary,
    }


def get_tech_news(amount):
    PAGE_URL = "https://www.tecmundo.com.br/novidades"
    current_page_content = fetch(PAGE_URL)
    news_links = scrape_novidades(current_page_content)

    while len(news_links) < amount:
        next_page = scrape_next_page_link(current_page_content)
        current_page_content = fetch(next_page)
        news_links.extend(scrape_novidades(current_page_content))

    news_links = news_links[:amount]

    scraped_news = []
    for news in news_links:
        news_html_content = fetch(news)
        scraped_notice = scrape_noticia(news_html_content)
        scraped_news.append(scraped_notice)

    create_news(scraped_news)
    return scraped_news
