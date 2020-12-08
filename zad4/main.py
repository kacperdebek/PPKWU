import requests
from bs4 import BeautifulSoup


url = 'https://panoramafirm.pl/szukaj?k=hydraulik&l='
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")

addresses = soup.findAll('div', {"class": "address"})
phone_numbers = soup.findAll('div', {"class": "icon-telephone"})
emails_and_names = soup.findAll('div', {"class": "ajax-modal-link"})

