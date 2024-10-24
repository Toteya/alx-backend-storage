#!/usr/bin/env python3
"""
10-update_topics
"""

def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name
    """
    query_filter = {"name":  name}
    update_operation = { "$set" :
        {"topics": topics}
    }
    mongo_collection.update_one(query_filter, update_operation)

