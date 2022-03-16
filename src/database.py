import asyncpg
from config import DB_URL, logger


class DB:
    @staticmethod
    async def create_coin_table(coin: str):
        try:
            conn: asyncpg.Connection = await asyncpg.connect(DB_URL)
            await conn.execute(f'''
                CREATE TABLE IF NOT EXISTS {coin}(
                    "time" bigint primary key,
                    "price" decimal
                );
            ''')
            return True
        except Exception as e:
            logger.error(f'CREATE TABLE "{coin}" ERROR: {e}')
            return False

    @staticmethod
    async def insert_coin_currency(coin: str, time: int, value: float):
        try:
            conn: asyncpg.Connection = await asyncpg.connect(DB_URL)
            await conn.execute(f'''
                INSERT INTO {coin}(time, price) VALUES($1, $2)
            ''', time, value)
            return True
        except Exception as e:
            logger.error(f'INSERT TO "{coin}" ERROR: {e}')
            return False
