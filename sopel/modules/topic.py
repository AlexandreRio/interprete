# -*- coding: utf-8 -*/
from sopel import module
from sopel.tools import events

@module.event('TOPIC')
@module.rule('(.*)')
def hook(bot, trigger):
  topic = trigger.args[1]
  if 'weekend' in topic or 'soir' in topic or 'w-e' in topic:
    bot.say("bdq, mettez les évènements dans le calendrier, pas en topic !")
