import urllib.request
import calendar
import os
#import locale

from datetime import datetime, timedelta
from pytz import timezone
from icalendar import Calendar, Event

from sopel import module

os.environ['TZ'] = 'Europe/Paris'
#TODO: install appropriate locale on the image
#locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
remote_cal = "https://kdoc.k0v1.xyz/remote.php/dav/public-calendars/5Q08PCZSSLP9Q2GQ?export"
local_cal = "calendar.ics"
lastseen = "lastseen.txt"

def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)

def printEvent(bot, component, begin, now):
    s = "* Le " + begin.strftime("%A %d à %Hh%m") +  "(dans " + strfdelta(begin-now,"{days} jours et {hours}h et {minutes} minutes") + "): " + component.get('summary') + ", " + component.get('location')
    bot.say (s)

def printAllDayEvent(bot, component, begin, now):
    s = "* Le " + begin.strftime("%A %d à %Hh%m") +  "(dans " + strfdelta(begin-now,"{days} jours") + "): " + component.get('summary') + ", " + component.get('location')
    bot.say (s)

@module.commands('kdoc')
def kdoc(bot, trigger):
    lastseenpath = ".sopel/" + lastseen
    lastget = 0
    if os.path.isfile(lastseenpath):
        with open(lastseenpath, 'r') as f:
            lastget = f.read()
        f.close()
    now = calendar.timegm(datetime.now(timezone('Europe/Paris')).utctimetuple())
    if ( (now - int(lastget)) > 3600):
        bot.say("I'm fetching the latest version of the calendar")
        urllib.request.urlretrieve(remote_cal, local_cal)
        with open(lastseenpath, 'w') as f:
            f.seek(0)
            f.write(str(now))
            f.truncate()
        f.close()


    g = open(local_cal,'rb')
    gcal = Calendar.from_ical(g.read())

    hasPrint = False
    for component in gcal.walk():
        if component.name == "VEVENT":
            now = datetime.now(timezone('Europe/Paris'))
            begin = component.decoded('dtstart')
            end = component.decoded('dtend')

            # TODO: check for recurring event with RRULE:FEQ=WEEKLY 
            # 'RRULE' : vRecur({'FREQ' : ['WEEKLY']})
            if (type(begin) is not datetime):
                now = datetime.now(timezone('Europe/Paris')).date()
                if (timedelta(days=0) < (begin - now) < timedelta(days=10)):
                    printAllDayEvent(bot, component, begin, now)
                    hasPrint = True
            else:
                if (timedelta(days=0) < (begin - now) < timedelta(days=10)):
                    printEvent(bot, component, begin, now)



            g.close()

    if not hasPrint:
        bot.say("No upcoming events, sorry")
