#!/usr/bin/env python3
"""This script analyzes Nginx request logs stored in a MongoDB collection 
and prints some statistics.
**Tasks:**
* **Task 12**: Analyze Nginx request logs
"""
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    """
        Prints various statistics about Nginx request logs in the provided collection.
    Args:
        nginx_collection: A pymongo collection object containing Nginx request logs.
    """
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        rq_cnt = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, rq_cnt))
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))


def run():
    """
    Connects to a MongoDB instance, retrieves the Nginx log collection, 
    and calls the print_nginx_request_logs function to display statistics.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)


if __name__ == '__main__':
    run()