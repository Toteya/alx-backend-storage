#!/usr/bin/env python3
"""
12-log_stats
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    all_docs = collection.count_documents({})
    get_docs = collection.count_documents({"method": "GET"})
    post_docs = collection.count_documents({"method": "POST"})
    put_docs = collection.count_documents({"method": "PUT"})
    patch_docs = collection.count_documents({"method": "PATCH"})
    delete_docs = collection.count_documents({"method": "DELETE"})

    print('{} logs'.format(collection.count_documents({})))
    print('Methods:')
    print('\tmethod GET: {}'.format(get_docs))
    print('\tmethod POST: {}'.format(post_docs))
    print('\tmethod PUT: {}'.format(put_docs))
    print('\tmethod PATCH: {}'.format(patch_docs))
    print('\tmethod DELETE: {}'.format(delete_docs))

    status_path_docs = collection.count_documents({"path": "/status"})

    print('{} status check'.format(status_path_docs))
