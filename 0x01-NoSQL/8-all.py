#!/usr/bin/env python3
"""8-all.py"""


def list_all(mongo_collection):
    """Lists all documents in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The PyMongo collection object.

    Returns:
        list: A list of documents or an empty list if no documents are found.
    """

    documents = list(mongo_collection.find())
    return documents
