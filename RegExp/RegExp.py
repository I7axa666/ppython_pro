import re
import csv

person_list = []
person_dict = {}

with open('phonebook_raw.csv',  encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

for contact in contacts_list[1:]:
    text = ','.join(contact)
    pattern = '(^[А-ЯЁ][а-я]+)\s?[,]?([А-ЯЁ][а-я]+)\s?[,]?([А-ЯЁ][а-я]+)?,([А-Яа-я]+)?,([А-Яа-я]+)?,?([А-Яа-я]+)?,?([^\d][а-яёА-ЯЁ][^,]*)?,?(\+7|8)?\s?\(?(\d{3})?\s?\)?\s?\-?(\d{3})?\-?(\d{2})?\-?(\d{2})?\s?\(?(доб\.)?\s?(\d{4})?\)?,?(.*)'
    lastname = re.sub(pattern, r'\1', text)
    firstname = re.sub(pattern, r'\2', text)
    surname = re.sub(pattern, r'\3', text)
    organization = re.sub(pattern, r'\6', text)
    position = re.sub(pattern, r'\7', text)
    phones = "". join(map(str, re.findall(r'\+?[7|8].*(?=,)', text)))

    if 'доб' in phones:
        phone = re.sub(r'(\+7|8)\s?\(?(\d{3})\)?\s?\-?(\d{3})\-?(\d{2})\-?(\d{2})\s?\(?([а-я]+\.\s?)?(\d{4})?\)?',
                       r'+7(\2)\3-\4-\5 доб.\7', phones)
    else:
        phone = re.sub(r'(\+7|8)\s?\(?(\d{3})\)?\s?\-?(\d{3})\-?(\d{2})\-?(\d{2})', r'+7(\2)\3-\4-\5', phones)

    mail = "". join(map(str, re.findall(r',([^,]\d?\w?.[^,]+@.+)', text)))
    my_list = []
    my_list = [lastname, firstname, surname, organization, position, phone, mail]
    lastname_firstname = lastname + firstname

    if lastname_firstname not in person_dict.keys():
        person_dict[lastname_firstname] = [lastname, firstname, surname, organization, position, phone, mail]
    else:
        index = 0
        for information in person_dict[lastname_firstname]:
            if information == '':
                person_dict[lastname_firstname][index] = my_list[index]
            index += 1

for_csv = [('lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'mail')]

for value in person_dict.values():
    for_csv.append(value)

with open("phonebook.csv", "w", encoding='utf-8', newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(for_csv)