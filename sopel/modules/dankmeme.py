# -*- coding: utf-8 -*/
from sopel import module

@module.rule(r'\blenny\b')
def lenny(bot, trigger):
  bot.say('( ͡° ͜ʖ ͡°)')

@module.rule(r'\bshrug\b')
def shrug(bot, trigger):
  bot.say('¯\_(ツ)_/¯')

@module.rule(r'\bdealwithit\b')
def dealwithit(bot, trigger):
    bot.say('☞   ͜ʖ  ☞')

@module.rule(r'\bdwi\b')
def dwi(bot, trigger):
    bot.say('(⌐■_■)')

@module.rule(r'\bkawai\b')
def kawai(bot, trigger):
    bot.say('ʢ◉ᴥ◉ʡ')

#I like it when it comes up on overwtach and other things
@module.rule(r'.*wat.*')
def wat(bot, trigger):
    bot.say('( ͡°_ ͡°)')

@module.rule(r'\bwaat\b')
def waat(bot, trigger):
    bot.say('staaap!')

@module.rule(r'\bgné\b')
def gne(bot, trigger):
    bot.say('ヽ(。_°)ノ')

@module.rule(r'\bftt\b')
def ftt(bot, trigger):
    bot.say('(╯°□°）╯︵ ┻━┻')

@module.rule(r'\bgodwin\b')
def godwin(bot, trigger):
    bot.say('\(°n°)')

@module.rule(r'\bRA+GE\b')
def rage(bot,trigger):
bot.say(' ┻━┻︵ \(°□°)/ ︵ ┻━┻')

@module.rule(r'\idkaidwtk\b')
def no(bot,trigger):
bot.say(' I don\'t know and I don\'t want to know ╭∩╮')

