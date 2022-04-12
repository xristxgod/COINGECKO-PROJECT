import asyncio
import json

from aiohttp import ClientSession

from config import logger, COINS, file_coins_top_100


async def download_top_100():
    async with ClientSession() as session:
        params = f'vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'
        async with session.get(
            f'https://api.coingecko.com/api/v3/coins/markets?{params}'
        ) as resp:
            if not resp.ok:
                logger.error(f'GET RESPONSE ERROR: {resp.status}')
                return None
            result = await resp.json()
    used_coins = []
    for_file = []
    for main_coin in COINS:
        for_file.append({
            "name": main_coin['name'],
            "symbol": main_coin['symbol'],
            "defaultPrice": main_coin['defaultPrice']
        })
        used_coins.append(main_coin['name'])
    for coin in result:
        if coin['id'] in used_coins:
            continue
        for_file.append({
            "name": coin['id'],
            "symbol": coin['symbol'],
            "defaultPrice": None
        })
        used_coins.append(coin['id'])
    with open(file_coins_top_100, "w", encoding="utf-8") as file:
        file.write(json.dumps(for_file))


if __name__ == '__main__':
    asyncio.run(download_top_100())
