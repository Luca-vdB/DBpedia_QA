# coding: utf-8

"""
Basic queries for dbpedia quepy.
"""

from refo import Group, Question, Plus
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Pos, QuestionTemplate


from dsl import *

class WhoIsTheOf(QuestionTemplate):
    """
    SELECT ?name 
    WHERE{
        ?body rdfs:label "England"@en.
        ?body  dbp:monarch ?monarch.
        ?monarch rdfs:label ?name
        FILTER (langMatches(lang(?name),"en"))
    }
    """
    role = Question(Pos("DT")) + Group(Plus(Pos("NN")| Pos("NNP")), "role")
    body = Question(Pos("DT")) + Group(Pos("NNP"), "body")  # Using proper noun
    regex = Lemma("who") + Lemma("be") + role + Lemma("of") + body + Question(Pos("."))

    def interpret(self, match):
        role = match.role.tokens
        body = match.body.tokens
       
        target = HasKeyword(body)
        person = NameIs(target)
        return person

    """
     def interpret(self, match):
        role = match.role.tokens
        body = match.body.tokens
        body_page = HasLabel(body)
        return body_page
    """