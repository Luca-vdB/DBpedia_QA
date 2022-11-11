# coding: utf-8

"""
Main script for dbpedia quepy.
"""

import quepy
dbpedia = quepy.install("dbpedia")
target, query, metadata = dbpedia.get_query("Who is the CEO of England?")
print(query)


from quepy.parsing import Lemma

print(Lemma("running"))