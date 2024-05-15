#!/usr/bin/env python3
"""12-log_stats"""
from pymongo import MongoClient
import pymongo

# Database and collection names
DATABASE_NAME = "logs"
COLLECTION_NAME = "nginx"

# Methods to count (modify if needed)
METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

# Path for status check
STATUS_PATH = "/status"


def connect_to_mongo():
  """Connects to the MongoDB database."""
  client = MongoClient()
  db = client[DATABASE_NAME]
  collection = db[COLLECTION_NAME]
  return collection


def count_documents(collection):
  """Counts the total number of documents in the collection."""
  count = collection.count_documents({})
  return count


def count_by_method(collection, methods):
  """Counts documents for each method in the provided list."""
  method_counts = {}
  for method in methods:
    count = collection.count_documents({"method": method})
    method_counts[method] = count
  return method_counts


def count_status_check(collection, path):
  """Counts documents where the path matches the status check path."""
  count = collection.count_documents({"path": path})
  return count


def print_stats(total_count, method_counts, status_count):
  """Prints the statistics in the expected format."""
  print(f"{total_count} logs")
  print("Methods:")
  for method, count in method_counts.items():
    print(f"\tmethod {method}: {count}")
  print(f"{status_count} status check")


if __name__ == "__main__":
  collection = connect_to_mongo()
  total_count = count_documents(collection)
  method_counts = count_by_method(collection, METHODS)
  status_count = count_status_check(collection, STATUS_PATH)
  print_stats(total_count, method_counts, status_count)
