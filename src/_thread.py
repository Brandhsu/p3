from concurrent.futures import ThreadPoolExecutor
import requests
import time
from timer import timeit
from config import URLS, DELAY


def job(url):
    resp = requests.get(url)
    resp.raise_for_status()

    text = resp.text
    # print("Downloaded {:,} characters.".format(len(text)))

    time.sleep(DELAY)
    return text


@timeit
def run(data: list):
    with ThreadPoolExecutor() as p:
        return p.map(job, data)


def save(filename, contents, root="bin/"):
    with open(root + filename, "w") as f:
        f.write(" ".join(list(contents)))


if __name__ == "__main__":
    result = run(URLS)

    from pathlib import Path

    save(Path(__file__).stem + ".txt", result)
