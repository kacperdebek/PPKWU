import requests
from bs4 import BeautifulSoup
url = 'http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok=2020&miesiac=10&lang=1'
r = requests.get(url)
print(r.text)
soup = BeautifulSoup(r.text, features="html.parser")
print(soup.find_all('a', href=True))
