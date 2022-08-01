import json
import datetime


def main():
    with open('competitors2.json', 'r', encoding='utf-8') as f:
        origin_competitors = json.loads(f.read())

    # В json файле перепутаны имена и фамилии, исправим это и удалим BOM символ
    competitors = {}
    for competitor_number in origin_competitors:
        competitors[competitor_number.lstrip('\ufeff')] = {'Name': origin_competitors[competitor_number]['Surname'],
                                                           'Surname': origin_competitors[competitor_number]['Name']}

    # Загружаем данные с результатами и сразу удаляем BOM символ
    with open('results_RUN.txt', 'r', encoding='utf-8') as res:
        results = res.readlines()
    results = [i.strip().lstrip('\ufeff').split() for i in results]

    # Создаем словарь с номером спортсмена и продолжительностью его забега
    competitors_results = {}
    for competitor_number, mark, time in results:
        time = time.replace(',', '.')
        if mark == 'start':
            competitors_results[competitor_number] = datetime.time.fromisoformat(time)
        elif mark == 'finish':
            # Так как нельзя просто найти разницу объектов datetime.time, то комбинируем их
            competitors_results[competitor_number] = datetime.datetime.combine(datetime.date.min,
                                                                               datetime.time.fromisoformat(time)) - \
                                                     datetime.datetime.combine(datetime.date.min,
                                                                               competitors_results[competitor_number])

    rating = sorted(competitors_results.items(), key=lambda item: item[1])
    # Выводим данные в формате "Занятое место Нагрудный номер Имя Фамилия Результат"
    for idx, (competitor_number, result) in enumerate(rating):
        print(idx + 1, competitor_number, competitors[competitor_number]['Name'],
              competitors[competitor_number]['Surname'], result)


if __name__ == '__main__':
    main()
