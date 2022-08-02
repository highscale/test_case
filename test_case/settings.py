import os

# base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# file with data competitors
COMPETITORS_JSON = os.path.join(BASE_DIR, "competitors2.json")

# file with data result run
RESULT_RUN_TXT = os.path.join(BASE_DIR, "results_RUN.txt")

# directory with temporary files
TEMP_DIR = os.path.join(BASE_DIR, "temp")

#temporary files
TEMP_JSON = os.path.join(TEMP_DIR, "results_competitors.json")
