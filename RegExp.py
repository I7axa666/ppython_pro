import re
from pprint import pprint
import csv
import sys
import os
import io
import json
from settings import CURRENT


current = CURRENT
file_name = 'phonebook_raw.csv'
full_path = os.path.join(current, file_name)


with open(full_path,  encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

pattern = '(^[А-ЯЁ][а-я]+)\s?[,]?([А-ЯЁ][а-я]+)\s?[,]?([А-ЯЁ][а-я]+)?,([А-Яа-я]+)?,([А-Яа-я]+)?,?([А-Яа-я]+)?,?([^\d][а-яёА-ЯЁ][^,]*)?,?(\+7|8)?\s?\(?(\d{3})?\s?\)?\s?\-?(\d{3})?\-?(\d{2})?\-?(\d{2})?\s?\(?(доб\.)?\s?(\d{4})?\)?,?(.*)'
contact_dict = {}

def normal(substitution, text):
    res = re.sub(pattern, substitution, text)
    return res

for contact in contacts_list[1:]:
    text = ','.join(contact)
    lastname_firstname = normal(r'\1 \2', text)
    inform = (normal(r'\3,\4,\5,\6,\7,+7(\9)\10-\11-\12,\14,\15', text).split(sep=','))
    inform = list(map(lambda x: x.replace('+7()--', ''), inform))
    # print(inform)
    if inform[6] != '':
        inform[5] = f'{inform[5]} доб.{inform[6]}'
        inform[6] = ''

    if lastname_firstname in contact_dict:
        n = 0

        for x in contact_dict[lastname_firstname]:
            if x in inform:
                n += 1
            else:
                inform[n] = contact_dict[lastname_firstname][n]
                n += 1
        contact_dict[lastname_firstname] = inform
    else:
        contact_dict[lastname_firstname] = inform
    # print(contact_dict)
for_csv = [['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']]

for k, v in contact_dict.items():
    person_list = list(k.split()) + v
    for_csv.append(person_list)

with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(for_csv)