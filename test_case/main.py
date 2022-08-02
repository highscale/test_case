import json
import os

from processings import ManageResult
import settings


class Main(ManageResult):
    """
    Data output
    """
    @staticmethod
    def del_temp_file():
        """
        Delete temp file
        :return:
        """
        os.remove(settings.TEMP_JSON)

    def get_result_rating(self):
        """
        Print data result of the race with the data of the runner
        :return: None
        """
        self.serializations_result()
        with open(settings.TEMP_JSON, encoding="utf-8") as results_competitors:
            data_results_competitors = json.load(results_competitors)
            sort_results_competitors = sorted(
                data_results_competitors.items(), key=lambda item: item[1]["time"]
            )
            for place, runner in enumerate(sort_results_competitors):
                print(
                    f"{place + 1} {runner[0]} {runner[1]['Name']} {runner[1]['Surname']} {runner[1]['time'][:-3]},{runner[1]['time'][-2:]}"
                )
        self.del_temp_file()


main = Main()
main.get_result_rating()
