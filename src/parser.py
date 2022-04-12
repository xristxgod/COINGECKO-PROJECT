from asyncio import sleep as async_sleep
from datetime import datetime
from typing import List

from config import logger
from .database import DB
from .client import client


async def get_currency_of_coins(coins: List[dict]) -> None:
    db = DB()
    await async_sleep(5)
    for coin in coins:
        await db.create_coin_table(coin["symbol"])

    currents = {}
    last_times = {}

    while True:
        all_results = await client.get_current_prices(','.join([coin["name"] for coin in coins]))

        for coin in coins:
            try:
                if coin['defaultPrice'] is not None:
                    is_without_gecko = True
                else:
                    is_without_gecko = False
                coin_name = coin["name"]
                if is_without_gecko:
                    currents.update({
                        coin_name: {'time': int(round(datetime.now().timestamp())), 'value': coin['defaultPrice']}
                    })
                    last_times.update({coin_name: currents[coin_name]['time']})
                    is_update = True
                else:
                    currents.update({coin_name: all_results[coin_name]})
                    is_update = currents[coin_name] is not None and (
                        (coin_name not in last_times.keys()) or (last_times[coin_name] != currents[coin_name]['time'])
                    )

                if is_update:
                    last_times.update({coin_name: currents[coin_name]['time']})
                    await db.insert_coin_currency(coin['symbol'], currents[coin_name]['time'], currents[coin_name]['value'])
            except Exception as e:
                logger.error(f'ERROR PARSING {coin["name"]}: {e}')
        await async_sleep(10)
