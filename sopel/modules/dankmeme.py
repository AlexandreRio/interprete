# -*- coding: utf-8 -*/
from sopel import module

@module.rule('(\W|\A)lenny(\W|\Z)')
def lenny(bot, trigger):
  bot.say('( ͡° ͜ʖ ͡°)')

@module.rule('(\W|\A)shrug(\W|\Z)')
def shrug(bot, trigger):
  bot.say('¯\_(ツ)_/¯')

@module.rule('(\W|\A)dealwithit(\W|\Z)')
def dealwithit(bot, trigger):
    bot.say('☞   ͜ʖ  ☞')

@module.rule('(\W|\A)dwi(\W|\Z)')
def dwi(bot, trigger):
    bot.say('(⌐■_■)')

@module.rule('(\W|\A)kawai(\W|\Z)')
def kawai(bot, trigger):
    bot.say('ʢ◉ᴥ◉ʡ')

#I like it when it comes up on overwtach
@module.rule('.*wat.*')
def wat(bot, trigger):
    bot.say('( ͡°_ ͡°)')

@module.rule('(\W|\A)waat(\W|\Z)')
def waat(bot, trigger):
    bot.say('staaap!')

@module.rule('(\W|\A)gné(\W|\Z)')
def gne(bot, trigger):
    bot.say('ヽ(。_°)ノ')

@module.rule('(\W|\A)ftt(\W|\Z)')
def ftt(bot, trigger):
    bot.say('(╯°□°）╯︵ ┻━┻')

@module.rule('(\W|\A)godwin(\W|\Z)')
def godwin(bot, trigger):
    bot.say('\(°n°)')

