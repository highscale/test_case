import json

import settings


class FileRunsTxt:
    """
    Open file with result run
    """

    def __init__(self):
        self.__results_run = settings.RESULT_RUN_TXT

    @property
    def result_run(self):
        return self.__results_run

    def open_file(self):
        """
        Get generator with list result
        """
        with (open(self.__results_run, "r", encoding="utf-8-sig")) as results_run:
            for result_run in results_run:
                yield result_run


class FileCompetitorsJson:
    """
    Open file with data competitors
    """

    def __init__(self):
        self.__competitors = settings.COMPETITORS_JSON
        self.__file_runs = FileRunsTxt()

    @property
    def competitors(self):
        return self.__competitors

    def write_file(self):
        """
        Get dict from file with data competitors
        """
        with open(self.__competitors, "r", encoding="utf-8") as competitors:
            data_competitors = json.load(competitors)
            return data_competitors
