# coding: utf-8

"""
Domain specific language for dbpedia quepy.
"""

from quepy.dsl import FixedRelation

class NameIs(FixedRelation):
    relation = "rdfs:label"
    reverse = True