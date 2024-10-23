#!/usr/bin/env python3
"""
module: 9-insert_school
"""

def insert_school(mongo_collection, **kwargs):
    """ Inserts a document into the given collection
    """
    doc = mongo_collection.insert_one({**kwargs})
    return doc.inserted_id
