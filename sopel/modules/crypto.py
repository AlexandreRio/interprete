# -*- coding: utf-8 -*/
import time
import requests

from sopel import module


@module.rule('.crypto')
def cryptocurr(bot, trigger):
    last_rates = bot.memory.get('crypto_rates', ([], 0))
    if time.time() - last_rates[1] > 300:
        bot.say("Updating rates, gimme a sec or two.")
        last_rates = (requests.get('https://api.coinmarketcap.com/v1/ticker/?convert=EUR&limit=5').json(), time.time())
    bot.memory['crypto_rates'] = last_rates
    bot.say(formats(last_rates[0]))


def formats(currencies):
    parts = list()
    for currency in currencies:
        if currency['percent_change_24h'].startswith('-'):
            parts.append('\x0304{}\x03 : {:.4f}€'.format(currency['symbol'], float(currency['price_eur'])))
        else:
            parts.append('\x0303{}\x03 : {:.4f}€'.format(currency['symbol'], float(currency['price_eur'])))
    return ' | '.join(parts)
