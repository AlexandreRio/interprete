#!/usr/bin/python
# -*- coding: utf-8 -*-
# \file cryptomacron.py
# \brief TODO
# \author Florent Guiotte <florent.guiotte@gmail.com>
# \version 0.2
# \date 17 sept. 2017
#
# TODO details

import time
import requests
import collections
import operator
from sopel import module

_starter = {'EUR' : 10000}
_nbcurrency = 100
_refresh_delay = 300

# HUD palette
class CMColor:
    reset = '\x03'
    good = '\x0311'
    bad = '\x0304'

def setup(bot):
    """Setup needed to patch memory structure when module is upgraded"""

    # v0.1 to v0.2
    rates = bot.memory.get('crypto_rates_cm', ({}, 0))
    if not isinstance(rates[0], dict):
        bot.memory['crypto_rates_cm'] = ({}, 0)

def get_rates_from_coinmarket(nbcurrency=10):
    new_rates = requests.get('https://api.coinmarketcap.com/v1/ticker/?convert=EUR&limit='+str(nbcurrency)).json()
    dic_rates = dict()
    for rate in new_rates:
        dic_rates[rate['symbol']] = rate
    return dic_rates

def get_rates(bot):
    last_rates = bot.memory.get('crypto_rates_cm', ({}, 0))
    if time.time() - last_rates[1] > _refresh_delay:
        new_rates  = last_rates[0]
        new_rates.update(get_rates_from_coinmarket(_nbcurrency))
        bot.memory['crypto_rates_cm'] = (new_rates, time.time())
    return last_rates[0]

def get_wallet(bot, trigger):
    nick = trigger.nick
    wallets = bot.memory.get('wallets', {})
    if not nick in wallets:
        wallets[nick] = _starter.copy()
    bot.memory['wallets'] = wallets
    return wallets[nick]

def get_curr(rates, curr):
    if curr in rates:
        return rates[curr]

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
    starter = _starter['EUR']

    scores = dict()
    for player, wallet in wallets.items():
        totalv = wallet['EUR']
        for k, v in sorted(wallet.items()):
            if k is not 'EUR':
                currency = get_curr(rates, k)
                value = float(currency['price_eur'])
                totalv += v * value
        scores[player] = totalv

    sorted_scores = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)

    line = list()
    for k, v in sorted_scores:
        score = v - starter
        if score >= 0:
            line.append('{}: {color.good}{:+.0f}{color.reset} €'.format(k, score, color=CMColor))
        else:
            line.append('{}: {color.bad}{:+.0f}{color.reset} €'.format(k, score, color=CMColor))

    bot.say(' | '.join(line))

if __name__ == "__main__":
    import readline
    import atexit

    histfile = ".python_history"
    try:
        readline.read_history_file(histfile)
        h_len = readline.get_current_history_length()
    except FileNotFoundError:
        open(histfile, 'wb').close()
        h_len = 0

    def save(prev_h_len, histfile):
        new_h_len = readline.get_current_history_length()
        readline.set_history_length(1000)
        readline.append_history_file(new_h_len - prev_h_len, histfile)
    atexit.register(save, h_len, histfile)

    class Bot:
        def __init__(self):
            self.memory = dict()

        def say(self, msg):
            print("[Bot] {}".format(msg))

    class Trigger:
        def __init__(self, nick):
            self.nick = nick

        def post(self, msg):
            self.msg = msg

        def split(self):
            return self.msg.split()

    bot = Bot()
    trg = Trigger('kara')
    setup(bot)

    # Frick
    trgf = Trigger('frick')
    trgf.post('.wallet')
    wallet_cm(bot, trgf)
    trgf.post('.buy 1 btc')
    buy_sell_cm(bot, trgf)

    read = str()
    while not read.startswith('.quit'):
        trg.post(read)
        if read.startswith('.wallet'):
            wallet_cm(bot, trg)
        elif read.startswith('.buy') or read.startswith('.sell'):
            buy_sell_cm(bot, trg)
        elif read.startswith('.traders'):
            high_scores(bot, trg)
        read = input('> ')
