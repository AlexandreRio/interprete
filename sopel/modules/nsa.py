#!/usr/bin/python
# -*- coding: utf-8 -*-
# \file %filename%.py
# \brief TODO
# \author Florent Guiotte <florent.guiotte@gmail.com>
# \version 0.1
# \date 18 avril 2017
#
# TODO details

from sopel import module
from urllib import request
import re

@module.commands('nsa')
def vote(bot, trigger):
    args = trigger.split()
    if len(args) > 1:
      if args[1] == 'kara':
        bot.say('he must be sleeping ¯\_(ツ)_/¯')
      elif args[1] == 'salvatoreG':
        queryServer(bot)
      else:
        bot.say('Hey, I don\'t know ' + ''.join(args[1:]))
    else:
      queryServer(bot)

def queryServer(bot):
      where = request.urlopen("https://whereis.alexrio.fr/").read().decode("utf-8")
      bot.say(re.sub(r'^I\'m ', 'salvatoreG is ', re.sub(r'^I ','salvatoreG ', where)))
