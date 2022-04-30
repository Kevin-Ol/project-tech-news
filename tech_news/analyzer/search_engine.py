import re
from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    # https://stackoverflow.com/questions/6266555/querying-mongodb-via-pymongo-in-case-insensitive-efficiently
    query = {"title": {"$regex": re.compile(title, re.IGNORECASE)}}
    found_news = search_news(query)
    return [(news["title"], news["url"]) for news in found_news]


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    query = {"timestamp": {"$regex": re.compile(date)}}
    found_news = search_news(query)
    return [(news["title"], news["url"]) for news in found_news]


def search_by_source(source):
    query = {"sources": {"$regex": re.compile(source, re.IGNORECASE)}}
    found_news = search_news(query)
    return [(news["title"], news["url"]) for news in found_news]


def search_by_category(category):
    query = {"categories": {"$regex": re.compile(category, re.IGNORECASE)}}
    found_news = search_news(query)
    return [(news["title"], news["url"]) for news in found_news]
