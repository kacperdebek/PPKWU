import requests

url = 'http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok=2020&miesiac=10&lang=1'
r = requests.get(url)
print(r.text)