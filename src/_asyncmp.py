import asyncio
from aiohttp import request
from aiomultiprocess import Pool
from timer import timeit
from config import URLS, DELAY


async def get(url):
    async with request("GET", url) as response:
        text = await response.text("utf-8")
        # print("Downloaded (more) {:,} characters.".format(len(text)))

        await asyncio.sleep(DELAY)
        return text


async def main(urls):
    async with Pool() as pool:
        results = await pool.map(get, urls)

    return results


@timeit
def run(data):
    return asyncio.run(main(data))


def save(filename, contents, root="bin/"):
    with open(root + filename, "w") as f:
        f.write(" ".join(list(contents)))


if __name__ == "__main__":
    result = run(URLS)

    from pathlib import Path

    save(Path(__file__).stem + ".txt", result)
