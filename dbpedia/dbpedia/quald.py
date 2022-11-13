from refo import Plus, Question
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Pos, QuestionTemplate, Particle
from .dsl import *


class Body(Particle):
    regex = Plus(Pos("DT") | Pos("NN") | Pos("NNS") | Pos("NNP") | Pos("NNPS"))

    def interpret(self, match):
        name = match.words.tokens.title()
        return HasKeyword(name)


class WhoIsTheCeoOf(QuestionTemplate):
    regex = Lemma("who") + Lemma("be") + Question(Pos("DT")) + (Lemma("ceo") | Lemma("Chief Executive Officer")) + Pos("IN") + Body() + Question(Pos("."))

    def interpret(self, match):
        key_people = KeyPeopleOf(match.body)

        return key_people, "enum"

class WhoIsTheMonarchOf(QuestionTemplate):
    regex = Lemma("who") + Lemma("be") + Question(Pos("DT")) + (Lemma("king") | Lemma("queen")) + Pos("IN") + Body() + Question(Pos("."))

    def interpret(self, match):
        monarch = MonarchOf(match.body)
        label = LabelOf(monarch)

        return label, "enum"

class WhoIsThePresidentOf(QuestionTemplate):
    regex = Lemma("who") + Lemma("be") + Question(Pos("DT")) + Lemma("president") + Pos("IN") + Body() + Question(Pos("."))

    def interpret(self, match):
        president = PresidentOf(match.body)
        incumbent = IncumbentOf(president)
        label = LabelOf(incumbent)

        return label, "enum"


class Place(Particle):
    regex = Plus(Pos("DT") | Pos("NN") | Pos("NNS") | Pos("NNP") | Pos("NNPS"))

    def interpret(self, match):
        name = match.words.tokens.title()
        return HasKeyword(name)


class InWhichCountryIsY(QuestionTemplate):
    regex = Pos("IN") + Lemma("which") + Lemma("country") + Lemma("be") + Place() + Question(Pos("."))

    def interpret(self, match):
        city = match.place
        country = CountryOf(city)
        label = LabelOf(country)

        return label, "enum"

class InWhichStateIsY(QuestionTemplate):
    regex = Pos("IN") + Lemma("which") + Lemma("state") + Lemma("be") + Place() + Question(Pos("."))

    def interpret(self, match):
        city = match.place
        country = StateOf(city)
        label = LabelOf(country)

        return label, "enum"


class WhatIsTheTimezoneOf(QuestionTemplate):
    regex = Lemma("what") + Lemma("be") + Question(Pos("DT")) + Lemma("time zone") + Lemma("of") + Place() + Question(Pos("."))

    def interpret(self, match):
        location = match.place
        timezone = TimezoneOf(location)
        label = LabelOf(timezone)

        return label, "enum"


class Person(Particle):
    regex = Plus(Pos("DT") | Pos("NN") | Pos("NNS") | Pos("NNP") | Pos("NNPS"))

    def interpret(self, match):
        name = match.words.tokens.title()
        return IsPerson + HasKeyword(name)


"""
class WhichArtistsWereBornOnTheSameDateAs(QuestionTemplate):
    regex = Lemma("which") + Lemma("artists") + Lemma("be") + Lemma("born") + Lemma("on") + \
        + Question(Pos("DT")) + Lemma ("same") + Lemma("date") + Lemma("as") + Person()

    def interpret(self, match):
        artist = match.person
        birthdate = BirthDayOf(artist)
        born_on = BornOn(birthdate)
        return born_on

"""




