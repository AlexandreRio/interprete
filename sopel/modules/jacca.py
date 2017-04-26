# -*- coding: utf-8 -*-
from sopel import module

@module.rule(r".*(?P<price>\b\d+\s*((po|pi[èe]ces?\s+d'or|euros?|dollars?)\b|(\$|€)))")
def deumilcincenpiesdor(bot, trigger):
    price = trigger.group('price')
    bot.say((
        "{price} ?! Eh... eh... C'est une blague ? {price}, mais où "
        "voulez-vous que je trouve {price}, dans le cul d'une vache ?!"
    ).format(price=price))
