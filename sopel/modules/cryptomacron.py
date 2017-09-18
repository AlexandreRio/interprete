#!/usr/bin/python
# -*- coding: utf-8 -*-
# \file cryptomacron.py
# \brief TODO
# \author Florent Guiotte <florent.guiotte@gmail.com>
# \version 0.1
# \date 17 sept. 2017
#
# TODO details

import time
import requests
import collections
from sopel import module

_starter = {'EUR' : 10000}
_nbcurrency = 5
_refresh_delay = 300

def get_rates(bot):
    last_rates = bot.memory.get('crypto_rates_cm', ([], 0))
    # TODO: create a strategy to get rates without UI delay
    if time.time() - last_rates[1] > _refresh_delay:
        #bot.say("Updating rates, gimme a sec or two.")
        last_rates = (requests.get('https://api.coinmarketcap.com/v1/ticker/?convert=EUR&limit='+str(_nbcurrency)).json(), time.time())
    bot.memory['crypto_rates_cm'] = last_rates
    return last_rates[0]

def get_wallet(bot, trigger):
    nick = trigger.nick
    wallets = bot.memory.get('wallets', {})
    if not nick in wallets:
        wallets[nick] = _starter.copy()
    bot.memory['wallets'] = wallets
    return wallets[nick]

def get_curr(rates, curr):
    for c in rates:
        if c['symbol'] == curr:
            return c

def transaction(wallet, rates, curr, amnt):
    currency = get_curr(rates, curr)
    if currency is None:
        return 'Unknown currency'
    value = float(currency['price_eur'])
    if amnt * value > wallet['EUR']:
        return 'You don\'t have enough €€€'
    if amnt + wallet.get(curr, 0) < 0:
        return 'You don\'t have enough ' + curr
    if not curr in wallet:
        wallet[curr] = amnt
    else:
        wallet[curr] += amnt
        if wallet[curr] == 0: wallet.pop(curr)
    wallet['EUR'] -= amnt * value
    return 'Done'

@module.commands('wallet')
def wallet_cm(bot, trigger):
    wallet = get_wallet(bot, trigger)
    rates = get_rates(bot)
    line = list()
    k, v = 'EUR', wallet['EUR']
    total = v
    line.append("{}: {:.2f}".format(k,v))
    for k, v in sorted(wallet.items()):
        if k is not 'EUR':
            currency = get_curr(rates, k)
            value = float(currency['price_eur'])
            total += v * value
            line.append("{}: {:}".format(k,v))

    line.append("Net value: {:.2f}".format(total))
    bot.say(' | '.join(line))

@module.commands('buy', 'sell')
def buy_sell_cm(bot, trigger):
    wallet = get_wallet(bot, trigger)
    rates = get_rates(bot)
    args = trigger.split()

    if len(args) < 3:
        bot.say("wrong input m8")
        return

    try:
        amnt = int(args[1])
        if amnt <= 0 : raise ValueError('qweqweqwe')
    except ValueError:
        bot.say("wrong value input m8")
        return

    amnt *= 1 + (args[0] == '.sell') * -2 # fuck ternary operators
    curr = args[2].upper()

    ret = transaction(wallet, rates, curr, amnt)
    bot.say(trigger.nick + ": "+ ret)

@module.commands('traders')
def high_scores(bot, trigger):
    wallets = bot.memory.get('wallets', {})
    rates = get_rates(bot)

    line = list()
    for player, wallet in wallets.items():
        line.append(player)

    bot.say(' | '.join(line))
