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
with open(file_coins, "r", encoding="utf-8") as file:
    COINS = json.loads(file.read())
POSTGRES_USER = environ.get('POSTGRES_USER', 'exchange_test')
POSTGRES_PASSWORD = environ.get('POSTGRES_PASSWORD', 'exchange_test')
POSTGRES_DATABASE = environ.get('POSTGRES_DATABASE', 'exchange_test')
POSTGRES_EXTERNAL_PORT = environ.get('POSTGRES_EXTERNAL_PORT', '5435')
POSTGRES_HOST = environ.get('POSTGRES_HOST', 'postgres-exchange')

DB_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DATABASE}'
