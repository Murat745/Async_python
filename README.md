import asyncio
import json
import time
import aiohttp


async def count1(session):
    print('example1')
    resp = await session.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
    json_data = await resp.json()
    for i in json_data:
        # j = json.load(i)
        if i.get('cc') == 'USD':
            return i.get('rate')


async def count2(session):
    print('example2')
    resp = await session.get('https://api.exchangerate.host/latest')
    json_data = await resp.json()
    return json_data.get('rates', {}).get('UAH')


async def count3(session):
    print('example3')
    resp = await session.get('https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur.json')
    json_data = await resp.json()
    return json_data.get('eur', {}).get('uah')


async def main():
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(count1(session), count2(session), count3(session))
        itog = sum(result)/3
        print(result)
        print(f'Average rate of UAH {itog}')


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f'{__file__} executed in {elapsed:0.2f} seconds.')