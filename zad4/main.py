import requests
from bs4 import BeautifulSoup
import vobject


def scrape_data(query):
    url = f'https://panoramafirm.pl/szukaj?k={query}&l='
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")

    addresses = soup.findAll('div', {"class": "address"})
    phone_numbers = soup.findAll('a', {"class": "icon-telephone"})
    emails_and_names = soup.findAll('a', {"class": "ajax-modal-link"})

    company_data = [{'name': name.get('data-company-name'),
                     'email': name.get('data-company-email'),
                     'phone': phone.get('title'),
                     'address': address.text.strip()} for name, phone, address in
                    zip(emails_and_names, phone_numbers, addresses)]
    return company_data


def generate_vcards(company_list):
    for company in company_list:
        vc = vobject.vCard()
        vc.add('fn').value = company['name']
        vc.add('email').value = company['email']
        vc.add('tel').value = company['phone']
        vc.add('adr').value = vobject.vcard.Address(company['address'])
        print(vc.serialize())


def generate_page(company_list):
    template = """
    <body>
        <table style="width:100%">
        <tr>
            <th>Company</th>
            <th>Email</th>
            <th>Address</th>
            <th>Phone</th>
            <th>Vcard</th>
        </tr>
    """
    for company in company_list:
        template += f"""
        <tr>
            <td>{company['name']}</td>
            <td>{company['email']}</td>
            <td>{company['address']}</td>
            <td>{company['phone']}</td>
            <td>"todo"</td>
        </tr>
        """
    template += """
        </table> 
        </body>
        """
    print(template)


generate_page(scrape_data("hydraulik"))
# generate_vcards(scrape_data("hydraulik"))
