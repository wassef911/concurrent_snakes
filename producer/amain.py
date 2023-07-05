import asyncio

import aiohttp


async def fetch_url(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


def main():
    pass


if __name__ == '__main__':
    main()  # next section explains the use of sys.exit
