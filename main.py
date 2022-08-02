import json
from datetime import datetime

with open('competitors2.json', 'r', encoding='utf-8') as names: # deserialization json
    names_new = json.load(names)

competition_result = dict()
number_player = ''
with open('results_RUN.txt', 'r', encoding='utf-8-sig') as result:
    for line in result:
        line = line.strip().split() # get a list of substrings
        number_player = line[0]
        if number_player in competition_result: # filling dictionary
            competition_result[number_player] = datetime.strptime(line[2], "%H:%M:%S,%f") - competition_result[
                number_player]
        else:
            competition_result[number_player] = datetime.strptime(line[2], "%H:%M:%S,%f")

competition_result_sorted = sorted(competition_result.items(), key=lambda x: x[1]) # sort value in dict
competition_result_sorted = dict(competition_result_sorted)

place = 1 # variable for place
print('Занятое место', ' ', 'Нагрудный номер', ' ', 'Имя', ' ', 'Фамилия' , ' ', 'Результат' )
for key in competition_result_sorted: # print results
    print(place, ' ', key, ' ', names_new[key]['Name'], ' ', names_new[key]['Surname'], ' ', competition_result_sorted[key])
    place += 1


