import json
from datetime import datetime

with open('competitors2.json', 'r', encoding='utf-8-sig') as file:
    competitors_list = json.load(file)
with open('results_RUN.txt', encoding='utf-8-sig') as file:
    times_list = file.read().split()
#Создание словаря с результатами попыток
timeslistdict = dict()
element = 0
for times_list[element] in times_list:
    if times_list[element].isdigit() and times_list[element] not in timeslistdict:
        start_time = datetime.strptime(times_list[element + 2], "%H:%M:%S,%f")
        finish_time = datetime.strptime(times_list[element + 5], "%H:%M:%S,%f")
        result_time = str(finish_time - start_time)
        result_time = result_time.replace('0:', '')
        timeslistdict[times_list[element]] = {'Time': result_time}
    element += 1
#Добавление в словарь со списком участников информации о результатах попыток
for element in competitors_list:
    if element in timeslistdict.keys():
        competitors_list[element].update(timeslistdict[element])
#Есть участник, который судя по файлу с результатами не стартовал его попытка будет признана не состоявшейся
    else:
        timeslistdict[element] = {'Time': 'No contest'}
        competitors_list[element].update(timeslistdict[element])
#Сортировка словаря по времени
competitors_list = dict(sorted(competitors_list.items(), key=lambda x: (x[1].get('Time'))))
#Добавление информации о занятом месте
place = 1
for element in competitors_list:
    competitors_list[element]['Place'] = place
    place += 1
#Вывод данных списком
list = []
for element in competitors_list:
    list.append(competitors_list[element]['Place'])
    list.append(element)
    list.append(competitors_list[element]['Name'])
    list.append(competitors_list[element]['Surname'])
    list.append(competitors_list[element]['Time'])
print(list)