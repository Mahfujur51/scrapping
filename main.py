from bs4 import BeautifulSoup
import requests
import  time
import  json
import csv
def find_companies():
    html_text = requests.get('https://medex.com.bd/companies?page=2')
    soup = BeautifulSoup(html_text.content, 'html.parser')
    # find_content = soup.find_all('a')
    find_contents =soup.find_all('div', class_ = 'col-xs-12 data-row-top')
    for company_name in find_contents:
        company_name = company_name.a.text
        # print(company_name)
        items = {
            'company name': company_name,
        }
        print(items)

    print(f'Json Data outpur successfully!!')

if __name__ == '__main__':
    while True:
        find_companies()
        time_wait=10
        time.sleep(time_wait*60)
