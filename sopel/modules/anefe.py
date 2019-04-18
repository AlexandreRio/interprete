# -*- coding: utf-8 -*/
from sopel import module

@module.rule('.*en effet.*')
def eneffet(bot, trigger):
  bot.say('anéfé')

@module.rule('.*anéfé.*')
def anefe(bot, trigger):
  bot.say('certes')

@module.rule('.*certes.*')
def certes(bot, trigger):
  bot.say('anéfé')

@module.rule('.*soldat.*')
def soldat(bot, trigger):
  bot.say('✋')

@module.rule(r".*est( plutôt)? fort.*")
def pomme(bot, trigger):
  bot.say('🍏 fort en pomme ?')
