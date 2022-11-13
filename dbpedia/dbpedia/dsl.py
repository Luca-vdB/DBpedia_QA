# coding: utf-8

# Copyright (c) 2012, Machinalis S.R.L.
# This file is part of quepy and is distributed under the Modified BSD License.
# You should have received a copy of license in the LICENSE file.
#
# Authors: Rafael Carrascosa <rcarrascosa@machinalis.com>
#          Gonzalo Garcia Berrotaran <ggarcia@machinalis.com>

"""
Domain specific language for DBpedia quepy.
"""

from quepy.dsl import FixedType, HasKeyword, FixedRelation

HasKeyword.relation = "rdfs:label"
HasKeyword.language = "en"


class IsCountry(FixedType):
    fixedtype = "dbo:Country"

class IsCompany(FixedType):
    fixedtype = "dbo:Company"


class LabelOf(FixedRelation):
    relation = "rdfs:label"
    reverse = True


class PresidentOf(FixedRelation):
    relation = "dbp:leaderTitle"
    reverse = True


class MonarchOf(FixedRelation):
    relation = "dbp:monarch"
    reverse = True


class IncumbentOf(FixedRelation):
    relation = "dbp:incumbent"
    reverse = True

class KeyPeopleOf(FixedRelation):
    relation = "dbp:keyPeople"
    reverse = True