#!/usr/bin/env python3
"""9-insert_school.py"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document into a MongoDB
       collection using keyword arguments.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The PyMongo collection object.
        **kwargs: Keyword arguments representingthe document
        fields and values.

    Returns:
        ObjectId: The ObjectId of the inserted document.
    """

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
