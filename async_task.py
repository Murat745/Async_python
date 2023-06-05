import aiohttp
import asyncio
import config
import time


async def count(session):
    print('example1')
    resp = await session.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')
    json_data = await resp.json()
    for i in json_data:
        if i.get('ccy') == 'USD':
            return float(i.get('sale'))


async def count_1(session):
    print('example2')
    resp = await session.get('https://api.exchangerate.host/latest')
    json_data = await resp.json()
    return json_data.get('rates', {}).get('UAH')


async def count_2(session):
    print('example3')
    resp = await session.get('http://apilayer.net/api/live?access_key=' + config.api_key + '&currencies=UAH&source'
                                                                                           '=USD&format=1')
    json_data = await resp.json()
    return json_data.get('quotes', {}).get('USDUAH')


async def main():
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(count(session), count_1(session), count_2(session))
        itog = sum(result)/3
        print(result)
        print(f'Average rate of UAH {itog}')


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f'{__file__} executed in {elapsed:0.2f} seconds.')
