from tech_news.database import get_collection


def top_5_news():
    collection = get_collection()
    pipeline = [
        {
            "$project": {
                "_id": False,
                "title": "$title",
                "url": "$url",
                "popularity": {"$sum": ["$shares_count", "$comments_count"]},
            }
        },
        {"$sort": {"popularity": -1}},
        {"$limit": 5},
    ]

    return [
        (news["title"], news["url"]) for news in collection.aggregate(pipeline)
    ]


def top_5_categories():
    collection = get_collection()
    pipeline = [
        {"$unwind": "$categories"},
        {"$group": {"_id": "$categories", "total": {"$sum": 1}}},
        {"$sort": {"total": -1, "_id": 1}},
        {"$limit": 5},
    ]

    return [news["_id"] for news in collection.aggregate(pipeline)]
