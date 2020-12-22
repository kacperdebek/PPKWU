import requests
from bs4 import BeautifulSoup
import vobject
from flask import Flask, send_file

app = Flask(__name__)


def scrape_data(query):
    url = f'https://panoramafirm.pl/szukaj?k={query}&l='
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")

    addresses = soup.findAll('div', {"class": "address"})
    phone_numbers = soup.findAll('a', {"class": "icon-telephone"})
    emails_and_names = soup.findAll('a', {"class": "ajax-modal-link"})

    company_data = [{'name': name.get('data-company-name') or "N/A",
                     'email': name.get('data-company-email') or "N/A",
                     'phone': phone.get('title') or "N/A",
                     'address': address.text.strip() or "N/A"} for name, phone, address in
                    zip(emails_and_names, phone_numbers, addresses)]
    return company_data


def generate_vcards(company_list):
    vcard_list = []
    for company in company_list:
        vc = vobject.vCard()
        vc.add('fn').value = company['name']
        vc.add('email').value = company['email']
        vc.add('tel').value = company['phone']
        vc.add('adr').value = vobject.vcard.Address(company['address'])
        vcard_list.append(vc.serialize())
    return vcard_list


def generate_page(company_list):
    generate_vcf_files(generate_vcards(company_list))
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
    for id, company in enumerate(company_list, 1):
        template += f"""
            <tr>
                <td>{company['name']}</td>
                <td>{company['email']}</td>
                <td>{company['address']}</td>
                <td>{company['phone']}</td>
                <td><a href="http://127.0.0.1:5000/vcf/files/company_{id}.vcf">wygeneruj VCard</a></td>
            </tr>
            """
    template += """
            </table> 
            </body>
            """
    f = open(f'mob.html', 'w', encoding="utf-8")
    f.write(template)
    f.close()


def generate_vcf_files(data):
    for num, company in enumerate(data, 1):
        f = open(f'files/company_{num}.vcf', 'w', encoding="utf-8")
        f.write(company)
        f.close()


generate_vcf_files(generate_vcards(scrape_data("hydraulik")))
generate_page(scrape_data("hydraulik"))


@app.route('/vcf/files/<filename>', methods=['GET'])
def vcf_generate(filename):
    return send_file(f'files/{filename}', mimetype="text/vcard")


@app.route('/vcf/<query>', methods=['GET'])
def html_endpoint(query):
    generate_page(scrape_data(query))
    return send_file("mob.html", mimetype="text/html")


app.run()
