import json
from datetime import datetime


def create_dict():
    with open('C:/Users/user/Desktop/appTest/test_case/competitors2.json', 'r', encoding='utf-8-sig') as file:
        list_of_people = json.load(file)
    with open('C:/Users/user/Desktop/appTest/test_case/results_RUN.txt', encoding='utf-8-sig') as file:
        Run_result = file.read().split()

    result_for_time = dict()
    count = 0
    for Run_result[count] in Run_result:
        if Run_result[count].isdigit() and Run_result[count] not in result_for_time:
            start_time = datetime.strptime(Run_result[count + 2], "%H:%M:%S,%f")
            finish_time = datetime.strptime(Run_result[count + 5], "%H:%M:%S,%f")
            result_time = str(finish_time - start_time)
            result_time = result_time.replace('0:', '')
            result_for_time[Run_result[count]] = {'Time': result_time}
        count += 1
    for element in list_of_people:
        if element in result_for_time.keys():
            list_of_people[element].update(result_for_time[element])
        else:
            result_for_time[element] = {'Time': 'Данный участник отсутствует в файле results_RUN'}
            list_of_people[element].update(result_for_time[element])

    members = dict(sorted(list_of_people.items(), key=lambda x: (x[1].get('Time'))))

    place = 1
    for i in members:
        members[i]['Place'] = place
        place += 1

    result = []
    for i in members:
        result.append(members[i]['Place'])
        result.append(i)
        result.append(members[i]['Surname'])
        result.append(members[i]['Name'])
        result.append(members[i]['Time'])
    print(result)

print(create_dict())