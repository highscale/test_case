import json
from datetime import datetime


def main(file_json, file_txt):
    # Функция вычисляет результат забега
    # Принимает два строковых параметра start_time и end_time
    # start_time - время начала забега
    # end_time - время окончания забега
    # Функция возвращает обрезанную строку равную разнице между началом и окончанием
    def calc_time(start_time: str, end_time: str) -> str:
        start = datetime.strptime(start_time, '%H:%M:%S,%f')
        end = datetime.strptime(end_time, '%H:%M:%S,%f')
        period = end - start
        return str(period)[2:-4].replace('.', ',')

    # Функция генерирует список данных о спортсмене
    # Принимает два параметра key типа int и value тип str
    # key - нагрудный номер спортсмена
    # value - результат забега
    # Функция возвращает список, который содержит имя, фамилию и результат забега
    def generate_list(key: int, value: str) -> list:
        values_list = list(data.get(str(key)).values())
        # переворот списка выполняется для установки правильного порядка имени и фамилии
        values_list.reverse()
        values_list.append(value)
        return values_list

    # кодировка utf-8-sig используется для удаления невидимого символа \ufeff
    with open(file_json, "r", encoding='utf-8-sig') as input_file_json:
        data = json.load(input_file_json)

    data_txt = []
    with open(file_txt, "r", encoding='utf-8-sig') as input_file_result:
        [data_txt.append(line.rstrip().split(' ')) for line in input_file_result]

    # генерация двух списков
    # start_data содержит данные о старте спорстменов
    # finish_data содержит данные о финише спорстменов
    start_data = [v for k, v in enumerate(data_txt) if not k % 2]
    finish_data = [v for k, v in enumerate(data_txt) if k % 2]

    # генерация словаря
    # ключ - нагрудный номер спортсмена
    # значение - результат забега
    dict_sportsmen = {start_data[i][0]: calc_time(start_data[i][2], finish_data[i][2])
                      for i in range(len(start_data))}

    # сортировка словаря по результатам забега
    sorted_dict_sportsmen = {key: value for key, value in sorted(dict_sportsmen.items(),
                                                                 key=lambda item: item[1])}

    # генерация словаря
    # ключ - нагрудный номер спортсмена
    # значение - список, который содержит имя, фамилию и результат забега
    final_dict = {key: generate_list(key, value) for key, value in sorted_dict_sportsmen.items()}

    with open('final_result.txt', 'w', encoding='utf-8-sig') as output_file:
        output_file.write(f"{'Занятое место ':10s} Нагрудный номер {'Имя':12s} {'Фамилия':12s} Результат\n")
        for i, (k, v) in enumerate(final_dict.items(), start=1):
            output_file.write(f'{i:7d} \t\t\t{k:10s} ')
            for item in v:
                output_file.write(f'{item:12s} ')

            output_file.write("\n")


if __name__ == '__main__':
    file_json = 'competitors2.json'
    file_txt = 'results_RUN.txt'
    main(file_json, file_txt)
