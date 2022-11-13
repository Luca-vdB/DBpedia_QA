# coding: utf-8

"""
Basic queries for dbpedia quepy.
"""

from refo import Group, Question, Plus
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Pos, QuestionTemplate, Particle, Token


from dsl import *

class Body(Particle):
    regex = Question(Pos("DT")) + Group(Pos("NNP"), "body")

    def interpret(self, match):
        name = match.body.tokens
        return NameIs(name)

class Role(Particle):
    regex = Group(Plus(Pos("NN")| Pos("NNP")), "role")  # Either a noun (e.g. king) or a proper noun like CEO

    def interpret(self, match):
        name = match.role.tokens
        print(name)
        return HasKeyword(name)

class Country(Particle):
    regex = Plus(Pos("DT") | Pos("NN") | Pos("NNS") | Pos("NNP") | Pos("NNPS"))

    def interpret(self, match):
        name = match.words.tokens.title()
        return IsCountry() + HasKeyword(name)


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
    role = Group(Plus(Pos("NN")| Pos("NNP")), "role")
    body = Question(Pos("DT")) + Group(Pos("NNP"), "body")  # Using proper noun
    #regex = Lemma("who") + Lemma("be") + Question(Pos("DT")) + Role() + Lemma("of") + Country() + Question(Pos("."))

    def interpret(self, match):
        role = match.role.tokens
        body = match.body.tokens
       
        target = HasKeyword(body)
        person = NameIs(target)
        return person
