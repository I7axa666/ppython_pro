import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import json
import re


def get_headers():

    headers = Headers(browser='firefox', os='win')
    return headers.generate()

item = {}
parsed = []
link = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'
pattern_city = '(^[А-ЯЁ][а-яё]+-?[А-ЯЁ]?[а-яё]+)'

for i in range(1, 5):
    response = requests.get(link, headers=get_headers())
    hh_main = response.text
    soup = BeautifulSoup(hh_main, features='lxml')
    article_list = soup.find('div', class_='main-content')
    articles = article_list.find_all('div', class_='vacancy-serp-item__layout')

    for article in articles:
        description = article.find(attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}).text
        if 'Django' and 'Flask' in description:
            link = article.find('a', class_='serp-item__title')['href']
            salary = article.find('span', class_='bloko-header-section-3')
            if salary == None:
                salary = ''
            else:

                if 'USD' in salary.text:
                    salary = salary.text.replace(u'\u202F', ' ')

                else:
                    sum = re.findall('\d+\s\d+\s?\d+?', salary.text)

                    s = u'\u202F'
                    if len(sum) > 1:
                        salary = f'{round(int(sum[0].replace(s, "")) / 70, 2)} - {round(int(sum[1].replace(s, "")) / 70, 2)} USD'
                    else:
                        salary = f'{round(int(sum[0].replace(s, "")) / 70, 2)} USD'
            company = article.find('a', class_='bloko-link bloko-link_kind-tertiary').text
            for_city = article.find(attrs={'data-qa': 'vacancy-serp__vacancy-address'}).text
            city = re.sub(pattern_city, r'\1', for_city)
            item = {
                'link': link,
                'salary': salary,
                'company': company.replace('\u00a0', ' '),
                'city': city.replace('\u00a0', ' ')
            }
            parsed.append(item)

    next = soup.find('a', {'data-qa': 'pager-next'})['href']
    link = f'https://spb.hh.ru{next}'
    i += 1

json_str = json.dumps(parsed, indent=5)

with open('hh.json', 'w', encoding='utf8') as f:
    json.dump(parsed, f, indent=5, ensure_ascii=False)
