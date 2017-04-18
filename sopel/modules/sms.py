#!/usr/bin/python
# -*- coding: utf-8 -*-
# \file %filename%.py
# \brief TODO
# \author Florent Guiotte <florent.guiotte@gmail.com>
# \version 0.1
# \date 15 avril 2017
#
# TODO details

from sopel import module
import requests

def setup(bot):
    if not 'smsclients' in bot.memory:
        bot.memory['smsclients'] = {}

@module.require_privmsg('This is a private command you dumb')
@module.commands('register')
def register(bot, trigger):
    """Register a free mobile account
    Enable \"Notifications par SMS\" option in your free account
    usage, in private message: .register [user] [key] (e.g. .register 12345876 ZqGhFwMIPeh07W)

    """
    if len(trigger.split()) != 3:
        bot.say("Use .help for usage")
        return

    args = trigger.group(2).split()
    user = args[0]
    key  = args[1]
    nick = trigger.nick

    if sendMessage(user, key, "From " + bot.nick + ": Hooray! It works."):
        bot.say("It works! I'm sending you a sms.")
        bot.say("I will text you each time someone call \".tell " + nick + "\".")
        addClient(bot, nick, user, key)
    else:
        bot.say("It is not working. Have you enabled \"Notifications par SMS\" in your account ?")

def addClient(bot, nick, user, key):
    bot.memory['smsclients'][nick] = (user, key)

def readClient(bot, nick):
    """Return user, key
    """
    account = bot.memory['smsclients'][nick]
    return account[0], account[1]

def sendMessage(user, key, msg):
    BASE_URL = 'https://smsapi.free-mobile.fr/sendmsg'
    params = {
        'user': user,
        'pass': key,
        'msg': msg
    }
    res = requests.get(BASE_URL, params=params)
    return res.status_code == 200

@module.commands('tell')
def smstrigger(bot, trigger):
    # Test if .tell command is valid
    if len(trigger.split()) != 3: return

    clients = bot.memory['smsclients']
    args = trigger.group(2).split()
    nick   = args[0]
    # Test if user exist in our dict
    if not nick in clients: return
    line   = ' '.join(args[1:])
    sender = trigger.nick #'Bernie'
    chan   = trigger.sender

    msg = "From " + chan + ", " + sender + ": " + line

    user, key = readClient(bot, nick)
    status = sendMessage(user, key, msg)
    #bot.say(str(status))
