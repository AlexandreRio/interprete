# -*- coding: utf-8 -*/
from sopel import module

@module.rule('(^|.? |\.)lenny( |$)')
def lenny(bot, trigger):
  bot.say('( ͡° ͜ʖ ͡°)')

@module.rule('(^|.? |\.)shrug( |$)')
def shrug(bot, trigger):
  bot.say('¯\_(ツ)_/¯')

@module.rule('(^|.? |\.)dealwithit( |$)')
def dealwithit(bot, trigger):
    bot.say('☞   ͜ʖ  ☞')

@module.rule('(^|.? |\.)dwi( |$)')
def dwi(bot, trigger):
    bot.say('(⌐■_■)')

@module.rule('(^|.? |\.)kawai( |$)')
def kawai(bot, trigger):
    bot.say('ʢ◉ᴥ◉ʡ')

#I like it when it comes up on overwtach and other things
@module.rule('.*wat.*')
def wat(bot, trigger):
    bot.say('( ͡°_ ͡°)')

@module.rule('(^|.? |\.)waat( |$)')
def waat(bot, trigger):
    bot.say('staaap!')

@module.rule('(^|.? |\.)gné( |$)')
def gne(bot, trigger):
    bot.say('ヽ(。_°)ノ')

@module.rule('(^|.? |\.)ftt( |$)')
def ftt(bot, trigger):
    bot.say('(╯°□°）╯︵ ┻━┻')

@module.rule('(^|.? |\.)godwin( |$)')
def godwin(bot, trigger):
    bot.say('\(°n°)')

@module.rule('(^|.? |\.)RA+GE( |$)')
def rage(bot,trigger):
    bot.say(' ┻━┻︵ \(°□°)/ ︵ ┻━┻')
