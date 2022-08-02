import json
from datetime import timedelta
from revelation_files import FileRunsTxt, FileCompetitorsJson
import settings


class ManageResult:
    """
    Processes data from results files
     and writes them to a temporary file
    """
    def __init__(self):
        self.__file_runs = FileRunsTxt()
        self.__file_competitors = FileCompetitorsJson()

    @property
    def file_runs(self):
        return self.__file_runs

    @property
    def file_competitors(self):
        return self.__file_competitors

    def get_dict_result(self, start_result, finish_result):
        """
        Get dict with runner result
        :param start_result: List
        :param finish_result: List
        :return: Dict
        """
        if (
            start_result[0] != finish_result[0]
            and start_result[1] == "start"
            and finish_result[1] == "finish"
        ):
            raise ValueError(
                f"Нарушена последовательность результатов в файле {self.file_runs.result_run}"
            )

        time_run = self.get_time_run(start_result[2], finish_result[2])
        dist_run = self.get_dist_run(start_result[3], finish_result[3])
        dict_result = {"time": time_run, "dist": dist_run}
        return dict_result

    @staticmethod
    def get_time_run(start_time, finish_time):
        """
        Get time race
        :param start_time: str
        :param finish_time: str
        :return: str
        """
        start_time = start_time.split(":")
        finish_time = finish_time.split(":")
        time_run = timedelta(
            hours=int(finish_time[0]),
            minutes=int(finish_time[1]),
            seconds=int(finish_time[2]),
        ) - timedelta(
            hours=int(start_time[0]),
            minutes=int(start_time[1]),
            seconds=int(start_time[2]),
        )
        return time_run.__str__()

    @staticmethod
    def get_dist_run(start_dist, finish_dist):
        """
        Get distance race
        :param start_dist: str
        :param finish_dist:str
        :return:int
        """
        dist_run = int(finish_dist) - int(start_dist)
        return dist_run

    def get_result_runner(self, dict_result, finish_result):
        """
        Get data of the runner from file with data competitors by number
        and combines them with the race data
        :param dict_result: Dict[str, str]
        :param finish_result: Dict[str, str]
        :return: Dict[str, Dict[str, str]]
        """
        result_runner = self.file_competitors.write_file().get(finish_result[0], None)
        result_runner.update(dict_result)
        result_runner = {finish_result[0]: result_runner}
        return result_runner

    @staticmethod
    def write_results_competitors(result_runner):
        """
        Writes the combined race and runner data to a file,
         if the file does not exist, then creates it
        :param result_runner: Dict[str, Dict[str, str]]
        :return: None
        """
        try:
            with open(settings.TEMP_JSON, encoding="utf-8") as results_competitors:
                data_results = json.load(results_competitors)
        except FileNotFoundError:
            with open(settings.TEMP_JSON, "x", encoding="utf-8"):
                data_results = result_runner
        data_results.update(result_runner)
        with open(settings.TEMP_JSON, "w", encoding="utf-8") as results_competitors:
            json.dump(data_results, results_competitors, indent=5, ensure_ascii=False)

    def serializations_result(self):
        """
        Union the result of the race with the data of the runner
         and writes it to a file
        :return: None
        """
        start_result = ""
        for finish_result in self.file_runs.open_file():
            finish_result = finish_result.replace(",", " ").split()
            if start_result:
                dict_result = self.get_dict_result(start_result, finish_result)
                result_runner = self.get_result_runner(dict_result, finish_result)
                self.write_results_competitors(result_runner)
                start_result = ""
                continue
            start_result = finish_result
