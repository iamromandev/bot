import random

from loguru import logger


class Proxy:

    def __init__(self):
        with open("src/data/input/proxies.txt", "r") as f:
            self.proxies = [proxy.strip() for proxy in f.readlines()]

        logger.info(self.proxies)

    def next_proxy(self) -> dict:
        proxy = random.choice(self.proxies)
        return {"http": f"http://{proxy}"}
