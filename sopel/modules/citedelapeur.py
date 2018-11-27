# -*- coding: utf-8 -*-
from sopel import module

@module.rule('Vous êtes .* \?')
def jsuislpape(bot, trigger):
    bot.say("Non j'suis l'pape et j'attends ma sœur !")
