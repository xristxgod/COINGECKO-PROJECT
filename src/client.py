from typing import Optional
from aiohttp import ClientSession
from config import logger, decimal


class Client:
    @staticmethod
    async def get_current_prices(coins: str) -> Optional[dict]:
        try:
            async with ClientSession() as session:
                params = f'ids={coins}&vs_currencies=usd&include_last_updated_at=true'
                async with session.get(
                        f'https://api.coingecko.com/api/v3/simple/price?{params}'
                ) as resp:
                    if not resp.ok:
                        logger.error(f'GET RESPONSE ERROR: {resp.status}')
                        return None
                    json = await resp.json()
                    result = {}
                    for coin_name in json.keys():
                        result.update({
                            coin_name: {
                                'value': decimal.create_decimal(json[coin_name]['usd']),
                                'time': json[coin_name]['last_updated_at']
                            }
                        })
            return result
        except Exception as e:
            logger.error(f'GET PRICE ERROR: {e}')
            return None


client = Client()
