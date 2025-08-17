import asyncio

from asyncio import Future
import random

import logging
logger = logging.getLogger(__name__)

async def task(i):
    x = random.randint(1, 5)
    logger.info("task %s, sleeping for %s", i, x)
    await asyncio.sleep(x)
    logger.info("task %s finished", i)
    if i > 4:
        raise ValueError("boom")
    return i

async def runner():
    futures:list[Future] = []
    for i in range(6):
        future = task(i)
        futures.append(future)

    futures = await asyncio.gather(*futures, return_exceptions=True)
    return futures


def main():
    results = asyncio.run(runner())
    for result in results:
        print(result, type(result))
        if isinstance(result, Exception):
            logger.error(result, exc_info=result)


if __name__ == "__main__":
    main()
    