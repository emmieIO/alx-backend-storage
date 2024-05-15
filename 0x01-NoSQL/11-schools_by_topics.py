#!/usr/bin/env python3
"""11-schools_by_topics.py"""


def schools_by_topic(mongo_collection, topic):
    """Returns a list of schools that have a specific
    topic in their list of topics.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The PyMongo collection object.
        topic (str):
        The topic to search for in the schools' lists.

    Returns:
        list: A list of dictionaries representing the
        matching school documents.
    """

    pipeline = [
        {"$match": {"topics": {"$in": [topic]}}},
        {"$project": {"_id": 0, "name": 1}}
    ]

    schools = list(mongo_collection.aggregate(pipeline))
    return schools
