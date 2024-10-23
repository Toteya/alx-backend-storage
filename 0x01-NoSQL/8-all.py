#!/usr/bin/env python3
"""
module 8-all
"""

def list_all(mongo_collection):
    """ Lists all documents in the given collection
    """
    documents_list =  mongo_collection.find()
    return documents_list
