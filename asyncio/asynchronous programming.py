import asyncio

import aiohttp

gists = ['https://gist.github.com/recluze/1d2989c7e345c8c3c542',
         'https://gist.github.com/recluze/a98aa1804884ca3b3ad3',
         'https://gist.github.com/recluze/5051735efe3fc189b90d',
         'https://gist.github.com/recluze/460157afc6a7492555bb',
         'https://gist.github.com/recluze/5051735efe3fc189b90d',
         'https://gist.github.com/recluze/c9bc4130af995c36176d']


async def get_gist(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            return len(text)


if __name__ == '__main__':
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    tasks = []
    for g in gists:
        future = asyncio.ensure_future(get_gist(g))
        tasks.append(future)

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    for result in tasks:
        print("Gist weight in kB is: {}".format(result.result()/1024))
