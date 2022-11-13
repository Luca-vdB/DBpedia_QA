# coding: utf-8

# Copyright (c) 2012, Machinalis S.R.L.
# This file is part of quepy and is distributed under the Modified BSD License.
# You should have received a copy of license in the LICENSE file.
#
# Authors: Rafael Carrascosa <rcarrascosa@machinalis.com>
#          Gonzalo Garcia Berrotaran <ggarcia@machinalis.com>

"""
Country related regex
"""

from refo import Plus, Question
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Pos, QuestionTemplate, Particle, Token
from .dsl import *


class Country(Particle):
    regex = Plus(Pos("DT") | Pos("NN") | Pos("NNS") | Pos("NNP") | Pos("NNPS"))

    def interpret(self, match):
        name = match.words.tokens.title()
        return IsCountry() + HasKeyword(name)

class Company(Particle):
    regex = Plus(Pos("DT") | Pos("NN") | Pos("NNS") | Pos("NNP") | Pos("NNPS"))

    def interpret(self, match):
        name = match.words.tokens.title()
        return IsCompany() + HasKeyword(name)


class WhoIsTheCeoOf(QuestionTemplate):
    regex = Lemma("who") + Lemma("be") + Question(Pos("DT")) + (Lemma("ceo") | Lemma("Chief Executive Officer")) + Pos("IN") + Company() + Question(Pos("."))

    def interpret(self, match):
        key_people = KeyPeopleOf(match.company)

        return key_people, "enum"

class WhoIsTheMonarchOf(QuestionTemplate):
    regex = Lemma("who") + Lemma("be") + Question(Pos("DT")) + (Lemma("king") | Lemma("queen")) + Pos("IN") + Country() + Question(Pos("."))

    def interpret(self, match):
        monarch = MonarchOf(match.country)
        label = LabelOf(monarch)

        return label, "enum"

class WhoIsThePresidentOf(QuestionTemplate):
    regex = Lemma("who") + Lemma("be") + Question(Pos("DT")) + Lemma("president") + Pos("IN") + Country() + Question(Pos("."))

    def interpret(self, match):
        president = PresidentOf(match.country)
        incumbent = IncumbentOf(president)
        label = LabelOf(incumbent)

        return label, "enum"







