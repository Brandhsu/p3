"""https://asherman.io/projects/unsync.html"""

import asyncio
import aiohttp
from unsync import unsync
from timer import timeit
from config import URLS, DELAY


@unsync
async def job(url):
    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        async with session.get(url) as resp:
            resp.raise_for_status()

            text = await resp.text()
            # print("Downloaded (more) {:,} characters.".format(len(text)))

            await asyncio.sleep(DELAY)
            return text


@timeit
def run(data: list):
    tasks = [job(d) for d in data]
    return [t.result() for t in tasks]


def save(filename, contents, root="bin/"):
    with open(root + filename, "w") as f:
        f.write(" ".join(list(contents)))


if __name__ == "__main__":
    result = run(URLS)

    from pathlib import Path

    save(Path(__file__).stem + ".txt", result)
