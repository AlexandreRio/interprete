import urllib.request
import collections
import calendar
import os
import locale

from datetime import datetime, timedelta
from pytz import timezone
from icalendar import Calendar, Event
from icalendar.prop import vCategory

from sopel import module

os.environ['TZ'] = 'Europe/Paris'
#TODO: install appropriate locale on the image
locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')
remote_cal="http://kdoc.guiotte.fr/remote.php/dav/public-calendars/QocpFySiCPRzyrx4?export"
local_cal = "calendar.ics"
lastseen = "lastseen.txt"
edit_url="https://kdoc.guiotte.fr/remote.php/dav/calendars/esir/esir_shared_by_florent/"
edit_user="esir"
edit_pass="yackisafaggot"

def removeVTIMEZONEBlock(f):
  ical = str("")
  match = False
  for line in f.readlines():
    if 'BEGIN:VTIMEZONE' in line:
      match = True

    if not match:
      ical += line

    if 'END:VTIMEZONE' in line:
      match = False

  return ical


def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)

def strmecomponent(component, wat, ifnone=''):
    rawstr = component.get(wat)
    if isinstance(rawstr, vCategory):
        return str(rawstr.to_ical().decode())

    if not rawstr.__class__ is list:
        return rawstr if rawstr is not None else ifnone
    else:
        nstr = rawstr.pop()
        #raw str can be a vCategory object afteral
        if isinstance(nstr, vCategory):
            nstr = str(nstr.to_ical().decode())

        for e in rawstr:
            if isinstance(e,vCategory):
                nstr = nstr + ", " + str(e.to_ical().decode())
            else:
                nstr = nstr + ", " + e
        return nstr

def createEvent(component, begin, now):
    location = component.get('location')
    localstr = location if location is not None else ''
    s = "‣ Le " + begin.strftime("\x02%A %d %B\x0F à %Hh%M") +  " (dans " + strfdelta(begin-now,"{days} jours et {hours}h et {minutes} minutes") + "): " + strfdetails(component, "\x02\x0304{summary}\x0F, {location} [\x0312{categories}\x03]")
    return s


def createAllDayEvent(component, begin, now):
    s = "‣ Le " + begin.strftime("\x02%A %d %B\x0F") +  " (dans " + strfdelta(begin-now,"{days} jours") + "): " + strfdetails(component, "\x02\x0304{summary}\x0F, {location} [\x0312{categories}\x03]")
    return s

def strfdetails(component, fmt):
    d = {"summary":    strmecomponent(component, "summary", "Untitled") }
    d["location"] =    strmecomponent(component, "location", "somewhere")
    d["categories"] =  strmecomponent(component, "categories", "Arck didn't do his job")
    d["uid"] =         strmecomponent(component, "uid")
    d["sequence"] =    strmecomponent(component, "sequence")
    d["description"] = strmecomponent(component, "description")
    return fmt.format(**d)

@module.rule('.*\.kdoc_setup.*')
def kdoc_setup(bot, trigger):
    """Setup informations to edit #esir calendar"""
    bot.say("To edit the calendar use a CalDAV/iCalendar client with this info:")
    bot.say("url: " + edit_url + " user: " + edit_user + " pass: " + edit_pass)

@module.commands('old_kdoc')
def kdoc(bot, trigger):
    bot.say("kdoc est cassé, il faut vois ça avec kara")

@module.rule('.*\.kdoc.*')
def old(bot, trigger):
    """Show #esir calendar next events, see .kdoc_setup"""
    args = trigger.split()
    if len(args) > 1 and args[1].isdigit():
      delta_days = int(args[1])
    else:
      delta_days = 20

    if delta_days > 90 or delta_days < 0 :
      bot.say("Don't even think about it")
      return

    lastseenpath = ".sopel/" + lastseen
    lastget = 0
    if os.path.isfile(lastseenpath):
        with open(lastseenpath, 'r') as f:
            lastget = f.read()
        f.close()
    now = calendar.timegm(datetime.now(timezone('Europe/Paris')).utctimetuple())
    if ( (now - int(lastget)) > 120):
        bot.say("I'm fetching the latest version of the calendar")
        urllib.request.urlretrieve(remote_cal, local_cal)
        with open(lastseenpath, 'w') as f:
            f.seek(0)
            f.write(str(now))
            f.truncate()
        f.close()


    g = open(local_cal,'r')
    gcal = Calendar.from_ical(removeVTIMEZONEBlock(g))

    eventDict = dict()
    for component in gcal.walk():
        if component.name == "VEVENT":
            now = datetime.now(timezone('Europe/Paris'))
            begin = component.decoded('dtstart')
            end = component.decoded('dtend')

            # TODO: check for recurring event with RRULE:FEQ=WEEKLY
            # 'RRULE' : vRecur({'FREQ' : ['WEEKLY']})
            if (type(begin) is not datetime):
                now = datetime.now(timezone('Europe/Paris')).date()
                newKey = datetime.combine(begin, datetime.min.time()).astimezone(timezone('Europe/Paris'))
                if (timedelta(days=0) < (begin - now) < timedelta(days=delta_days)):
                    if not begin in eventDict:
                        eventDict[newKey] = list()
                    eventDict[newKey].append(createAllDayEvent(component, begin, now))
            else:
                begin = begin.astimezone(timezone('Europe/Paris'))
                if (timedelta(days=0) < (begin - now) < timedelta(days=delta_days)):
                    if not begin in eventDict:
                       eventDict[begin] = list()
                    eventDict[begin].append(createEvent(component, begin, now))
    g.close()

    if not eventDict:
        bot.say("No upcoming events, sorry")
    else:
        for k,v in enumerate(dict(sorted(eventDict.items()))):
          for ev in eventDict[v]:
            bot.say(str(ev))
