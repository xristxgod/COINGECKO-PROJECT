import json
from logging import getLogger
from os import environ, path, listdir, mkdir
from decimal import Context


decimal = Context()
decimal.prec = 14

logger = getLogger(__name__)

ROOT_DIR = path.dirname(path.abspath(__file__))
BASE_DIR = path.join(ROOT_DIR, "files")
if "files" not in listdir(ROOT_DIR):
    mkdir(BASE_DIR)

file_coins = path.join(BASE_DIR, 'coins.json')
file_coins_top_100 = path.join(BASE_DIR, 'coins_top_100.json')

with open(file_coins, "r", encoding="utf-8") as file:
    COINS = json.loads(file.read())
with open(file_coins_top_100, "r", encoding="utf-8") as file:
    COINS_TOP_100 = json.loads(file.read())

POSTGRES_USER = environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = environ.get('POSTGRES_PASSWORD')
POSTGRES_DATABASE = environ.get('POSTGRES_DATABASE')
POSTGRES_EXTERNAL_PORT = environ.get('POSTGRES_EXTERNAL_PORT')
POSTGRES_HOST = environ.get('POSTGRES_HOST')

DB_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DATABASE}'
