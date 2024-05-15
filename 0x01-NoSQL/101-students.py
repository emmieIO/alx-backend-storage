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
          "$unwind": "$scores"
        },
        {
          "$group": {
              "_id": "$_id",
              "averageScore": {"$avg": "$scores.score"}
            }
        },
        {
          "$sort": {"averageScore": -1}
        }
    ]

    aggregation = AggregationPipeline(pipeline)
    return mongo_collection.aggregate(aggregation)
