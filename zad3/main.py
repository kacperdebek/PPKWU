import requests
from bs4 import BeautifulSoup

url = 'http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok=2020&miesiac=10&lang=1'
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")

calendar_days = soup.find_all('a', href=True)[2:]

calendar_dict = {elem.text: elem.get('href') for elem in calendar_days}

print(calendar_dict)
