import requests
from bs4 import BeautifulSoup

url = 'https://panoramafirm.pl/szukaj?k=hydraulik&l='
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")

addresses = soup.findAll('div', {"class": "address"})
phone_numbers = soup.findAll('a', {"class": "icon-telephone"})
emails_and_names = soup.findAll('a', {"class": "ajax-modal-link"})

company_data = [{'name': name.get('data-company-name'),
                 'email': name.get('data-company-email'),
                 'phone': phone.get('title'),
                 'address': address.text.strip()} for name, phone, address in zip(emails_and_names, phone_numbers, addresses)]
print(company_data)