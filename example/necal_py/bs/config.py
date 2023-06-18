import os

BASE_DIR = os.path.join(os.path.dirname(__file__))
CALENDAR_PATH = os.path.join(BASE_DIR, '../data', 'bs.csv')
REFERENCE_DATE_AD = {'year': 1918, 'month': 4, 'day': 13}
MIN_DATE = {'year': 1975, 'month': 1, 'day': 1}
MAX_DATE = {'year': 2100, 'month': 12, 'day': 30}
