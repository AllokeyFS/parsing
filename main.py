import csv
import requests
from bs4 import BeautifulSoup
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
urls = []
for n in range(1, 162):
    urls.append(f'')


with open('laptop.csv', 'w', newline='', encoding='utf-8') as data:
    writer = csv.writer(data)
    writer.writerow(['Name', 'Description', 'Price','URL'])

    for url in urls:
        req = requests.get(url, headers=headers)
        bs4 = BeautifulSoup(req.text, 'html.parser')
        items = bs4.findAll('div', class_='item product_listbox oh')

        for item in items:
            name = item.find('div', class_='listbox_title oh').get_text(strip=True).strip('Сотовый телефон ')
            description = item.find('div', class_='product_text pull-left').get_text(strip=True)
            price = item.find('div', class_='listbox_price text-center').get_text(strip=True)
            writer.writerow([name, description, price,url])