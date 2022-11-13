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


class IsPerson(FixedType):
    fixedtype = "foaf:Person"

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

class CountryOf(FixedRelation):
    relation = "dbo:country"
    reverse = True

class StateOf(FixedRelation):
    relation = "dbo:federalState"
    reverse = True

class TimezoneOf(FixedRelation):
    relation = "dbo:timeZone"
    reverse = True

class BirthDayOf(FixedRelation):
    relation = "dbo:birthDate"
    reverse = True

class BornOn(FixedRelation):
    relation = "dbo:birthDate"

class IsArtist(FixedType):
    fixedtype = "dbo:Artist"

    