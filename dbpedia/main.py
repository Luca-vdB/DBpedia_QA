# coding: utf-8

"""
Main script for dbpedia quepy.
"""

import quepy


dbpedia = quepy.install("dbpedia")


target, query, metadata = dbpedia.get_query("Who is president of France?")
print(query)
target, query, metadata = dbpedia.get_query("Who is queen of England?")
print(query)
target, query, metadata = dbpedia.get_query("Who is the CEO of Sony?")
print(query)