from requests import get
from bs4 import BeautifulSoup
from csv import DictReader, DictWriter, reader
from time import sleep


start_url = "https://napavintners.com/wineries/all_wineries.asp"
base_url = 'https://napavintners.com/'

with open('wineries.csv', 'w', newline='') as file:
    headers = ['Name', 'Address', 'Email', 'Details']
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    res = get(f'{start_url}')
    print(f'Now scraping {start_url}')
    soup = BeautifulSoup(res.text, 'html.parser')
    wineries = soup.find_all(class_="span8")
    for w in wineries:
        details = w.find('a')['href']
        detailed_res = get(f'{base_url}{details}')
        detailed_soup = BeautifulSoup(detailed_res.text, 'html.parser')
        name_obj = detailed_soup.find('h2')
        if name_obj:
            name = name_obj.get_text()
            email = detailed_soup.find(class_="winery-links")('a')[1]['href']
            csv_writer.writerow({
                'Name': name,
                "Address": ' ',
                'Email': email,
                "Details": details
            })
            print(f'Now getting info for {name}')
            sleep(0.5)
        else:
            print('Invalid Vienyard. Moving on.')

