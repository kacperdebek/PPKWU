import requests
from bs4 import BeautifulSoup
from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC  # timezone


def create_calendar(l):
    cal = Calendar()

    for ev in l:
        event = Event()
        event.add('summary', ev[2])
        event.add('dtstart', datetime(2020, 11, int(ev[0]), 0, 0, 0, tzinfo=UTC))
        event.add('dtend', datetime(2020, 11, int(ev[0]), 23, 0, 0, tzinfo=UTC))
        event.add('description', ev[1])
        cal.add_component(event)

    f = open('calendar.ics', 'wb')
    f.write(cal.to_ical())
    f.close()


url = 'http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok=2020&miesiac=10&lang=1'
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")
print(r.text)
calendar_days = soup.find_all('a', href=True)[2:]
event_names = soup.find_all('div', {"class": "InnerBox"})
for elem in event_names:
    print(elem.text)

calendar_dict = [[elem.text, elem.get('href')] for elem in calendar_days if elem.get('href') != "javascript:void();"]
for elem in calendar_dict:
    elem.append(event_names.pop(0).text)

create_calendar(calendar_dict)
