# -*- coding: utf-8 -*-
from sopel import module

currencies = [
    "po", "pi[èe]ces? d'or", "dollars?", "euros?",
    "boules?", "balles?", "francs?", "briques?", "patates?",
    "bucks?", "sesterces?", "ronds?", "centimes?", "cents?",
    "sacs?", "sous?", "sucres?", "livres?",
]
currency_symbs = [r'\$', '€', '£', '¢']

price_regex = r".*(?P<price>\b\d+\s*(({})\b|({})))".format(
    '|'.join(currencies), '|'.join(currency_symbs))


@module.rule(price_regex)
def deumilcincenpiesdor(bot, trigger):
    price = trigger.group('price')
    bot.say((
        "{price} ?! Eh... eh... C'est une blague ? {price}, mais où "
        "voulez-vous que je trouve {price}, dans le cul d'une vache ?!"
    ).format(price=price))
