# -*- coding: utf-8 -*-
from sopel import module


@module.rule(r".*\bj'en ai marre\b")
def lamarocanar(bot, trigger):
    bot.say("Comme la mare aux canards ?")


@module.rule(r".*\bcamouflage\b")
def camouflajcaca(bot, trigger):
    bot.say("Camouflage caca")


@module.rule(r".*\bà qui\b")
def akadoc(bot, trigger):
    bot.say("À Kadoc !")
