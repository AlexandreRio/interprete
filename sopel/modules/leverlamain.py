# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from sopel import module


@module.rule(r'^quand je dirai le mot "?soldat"?, vous lèverez la main[.! ]*$')
def soldat_activate(bot, trigger):
    bot.memory['soldat_activate_date'] = datetime.now()


@module.rule(r'.*\bsoldat\b.*')
def soldat(bot, trigger):
    soldat_date = bot.memory.get('soldat_activate_date')
    if soldat_date and datetime.now() - timedelta(minutes=15) < soldat_date:
        bot.say("/me lève la main")


@module.rule(r'^interprete: lève la main[.! ]*$')
def levelamain(bot, trigger):
    bot.say("{}: t'as pas dit jacadi !".format(trigger.nick))


@module.rule(r'^interprete: (jacc?add?i|jacca dit|jacques a dit):? '
             r'"?lève la main"?[.! ]*$')
def jacadilevelamain(bot, trigger):
    bot.action("lève la main")
