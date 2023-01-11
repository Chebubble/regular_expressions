from pprint import pprint
import csv
import re

pattern = r"[\+7|8]*[\s\(]*(\d{3})[\)\-\s]*(\d{3})[\-]*(\d{2})[\-]*(\d{2})[\s\()]*(\w+\.)?[\s]*(\d+)?[\)]*"
sub = r'+7(\1)\2-\3-\4 \5\6'
# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


def ordering(contacts_list: list) -> list:
    new_list = []
    for i in contacts_list:
        item = ' '.join(i[:3]).split(' ')
        res = [item[0], item[1], item[2], i[3], i[4], re.sub(pattern, sub, i[5]), i[6]]
        new_list.append(res)
    return union(new_list)


def union(new_list: list) -> list:
     for item in new_list:
        for new_item in new_list:
             if item[0] == new_item[0] and item[1] == new_item[1]:
                 if item[2] == '': item[2] = new_item[2]
                 if item[3] == '': item[3] = new_item[3]
                 if item[4] == '': item[4] = new_item[4]
                 if item[5] == '': item[5] = new_item[5]
                 if item[6] == '': item[6] = new_item[6]
     result_list = []
     for item in new_list:
         if item not in result_list:
             result_list.append(item)
     return (result_list)

with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(ordering(contacts_list))
