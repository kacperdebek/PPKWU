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


def get_calendar_data(month):
    url = f'http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok=2020&miesiac={month}&lang=1'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    calendar_days = soup.find_all('a', {"class": "active"})
    event_names = soup.find_all('div', {"class": "InnerBox"})

    calendar_dict = [[elem.text, elem.get('href')] for elem in calendar_days]
    for elem in calendar_dict:
        elem.append(event_names.pop(0).text)
    return calendar_dict

# create_calendar(calendar_dict)
