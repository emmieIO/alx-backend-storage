#!/usr/bin/env python3
"""10-update_topics"""


def update_topics(mongo_collection, name, topics):
    """Updates the topics field of
    all school documents with the matching name.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The PyMongo collection object.
        name (str): The name of the school to update documents for.
        topics (list): The new list of topics to be set.

    Returns:
        int: The number of documents updated.
    """

    update_result = mongo_collection.update_many(
        {"name": name}, {"$set": {"topics": topics}}
    )
    return update_result.modified_count
