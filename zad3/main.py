import requests
from bs4 import BeautifulSoup
from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC  # timezone

url = 'http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok=2020&miesiac=10&lang=1'
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")
print(r.text)
calendar_days = soup.find_all('a', href=True)[2:]
event_names = soup.find_all('div', {"class": "InnerBox"})
for elem in event_names:
    print(elem.text)

calendar_dict = [[elem.text, elem.get('href')] for elem in calendar_days]
for elem in calendar_dict:
    if elem[1] == "javascript:void();":
        elem.append("")
    else:
        elem.append(event_names.pop(0).text)

print(calendar_dict)



