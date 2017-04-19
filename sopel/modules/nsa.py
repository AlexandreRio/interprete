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
    where = request.urlopen("https://whereis.alexrio.fr/").read().decode("utf-8")
    bot.say(re.sub(r'^I\'m ', 'salvatoreG is ', re.sub(r'^I ','salvatoreG ', where)))
