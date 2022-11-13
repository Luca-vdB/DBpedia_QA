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
from quepy.parsing import Lemma, Pos, QuestionTemplate, Token, Particle
from .dsl import IsCountry, IncumbentOf, \
    LabelOf, PresidentOf


class Body(Particle):
    regex = Plus(Pos("DT") | Pos("NN") | Pos("NNS") | Pos("NNP") | Pos("NNPS"))

    def interpret(self, match):
        name = match.words.tokens.title()
        return IsCountry() + HasKeyword(name)

class Role(Particle):
    # For now either president or monarch
    regex = Question(Pos("DT")) + Plus(Pos("NN") | Pos("NNP"))

    def interpret(self, match):
        name = match.words.tokens.title()
        return 


class WhoIsTheXOfY(QuestionTemplate):

    regex = Lemma("who") + Lemma("be") + Role() + Pos("IN") + Body() + Question(Pos("."))

    def interpret(self, match):
        president = PresidentOf(match.body)
        incumbent = IncumbentOf(president)
        label = LabelOf(incumbent)

        return label, "enum"







