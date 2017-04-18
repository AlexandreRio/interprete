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

@module.commands('nsa')
def vote(bot, trigger):
    where = request.urlopen("https://whereis.alexrio.fr/").read().decode("utf-8")
    bot.say("salvatoreG is " + where[4:])
