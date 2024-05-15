#!/usr/bin/env python3
"""101-students.py"""
from pymongo import AggregationPipeline


def top_students(mongo_collection):
    """
        Returns all students from
        the collection sorted by average score.

    Args:
        mongo_collection: A pymongo collection object.

    Returns:
        A cursor object containing
        documents with student information and
        a new key "averageScore" for the
        average score.
    """
    pipeline = [
        {
            '$project': {
                '_id': 1,
                'name': 1,
                'averageScore': {
                    '$avg': {
                    '$avg': '$topics.score',
                    },
                },
                'topics': 1,
            },
        },
        {
            '$sort': {'averageScore': -1},
        },
    ]

    aggregation = AggregationPipeline(pipeline)
    return mongo_collection.aggregate(aggregation)
