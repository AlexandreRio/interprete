# -*- coding: utf-8 -*-
from sopel import module


@module.rule(r".*\baprès(\s|-)demain\b")
def apresdemain(bot, trigger):
    bot.say("Après demain, à partir d'aujourd'hui ?")


@module.rule(r"et toc\s*!?$")
def ettoc(bot, trigger):
    bot.say("Remonte ton slibard, Lothard !")


@module.rule(r".*\bfédér(ée?s?|er)\b")
def federer(bot, trigger):
    if not bot.memory.get('federer'):
        bot.say("Encore, pfff...")
        bot.memory['federer'] = 1


@module.rule(r"(interprete:\s*)?quoi\s+encore\s*\??$")
def federer2(bot, trigger):
    if bot.memory.get('federer') == 1:
        bot.say("Ben j'en ai marre. Ça revient à chaque fois sur le tapis ça.")
        bot.memory['federer'] = 2


@module.rule(r"(interprete:\s*)?quoi\s+ça\s*\??$")
def federer3(bot, trigger):
    if bot.memory.get('federer') == 2:
        bot.say(
            "Fédéré! D'habitude j'dis rien mais là zut ! J'sais pas c'que ça "
            "veut dire. Moi j'veux bien faire des efforts pour comprendre les "
            "réunions mais faut que chacun y mette du sien aussi. Là on est "
            "partis pour une heure avec des fédérés par-ci des fédérés "
            "par-là, j'vais encore rien biter et ça me gonfle."
        )
        bot.memory['federer'] = 3


@module.rule(r".*\b(rallier|Kaamelott|clans?|centraliser|commune?s?)\b")
def federer4(bot, trigger):
    if bot.memory.get('federer') == 3:
        bot.say("Si c'est ça encore ça va...")
        bot.memory['federer'] = 0
