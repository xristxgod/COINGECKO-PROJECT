import asyncio
from src.parser import get_currency_of_coins
from config import COINS


async def main():
    await get_currency_of_coins(COINS)


if __name__ == '__main__':
    asyncio.run(main())
