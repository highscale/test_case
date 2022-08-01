from datetime import datetime
import json

def main(address1, address2):
    with open(address1) as file:
        lines = file.read().splitlines()
    dic_start = {}
    dic_finish = {}
    for line in lines:
        num, SF, time = line.split()
        if SF == 'start':
            dic_start.update({num: time})
        elif SF == 'finish':
            dic_finish.update({num: time})

    dic_interfal = {}
    for num_start in dic_start:
        for num_finish in dic_finish:
            if num_start == num_finish:
                time_start = datetime.strptime(dic_start[num_start], "%H:%M:%S,%f")
                time_finish = datetime.strptime(dic_finish[num_finish], "%H:%M:%S,%f")
                time_interfal = time_finish - time_start
                dic_interfal.update({num_start: time_interfal})

    sorted_tuple = sorted(dic_interfal.items(), key=lambda x: x[1])
    sorted_tuple
    dict(sorted_tuple)
    place = 1
    y = 0
    for i in sorted_tuple:
        name_surname = json_name(address2)
        number = sorted_tuple[y][0]
        time = sorted_tuple[y][1]
        name = str(name_surname[number]['Name'])
        surname = str(name_surname[number]['Surname'])
        print(place, number, name, surname, time)
        place = place + 1
        y = y + 1

def json_name(address):
    with open(address) as fp:
        data = json.load(fp)
        return data

if __name__ == '__main__':
    address_results_RUN = ('./results_RUN.txt')
    address_competitors2 = ('./competitors2.json')
    main(address_results_RUN, address_competitors2)


