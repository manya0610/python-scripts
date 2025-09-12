import logging
import time
from concurrent.futures import Future, ThreadPoolExecutor

logger = logging.getLogger(__name__)


def task(i):
    logger.info("task %s, sleeping for %s", i, i)
    time.sleep(i)
    logger.info("task %s finished", i)
    if i > 4:
        raise ValueError("boom")
    return i


def main():
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures: list[Future] = []
        for i in range(6):
            future = executor.submit(task, (i))
            futures.append(future)

    print("done")
    for future in futures:
        try:
            result = future.result()
            print(result)
        except Exception as e:
            logger.error("error", exc_info=e)


if __name__ == "__main__":
    main()
