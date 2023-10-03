from loguru import logger
from fastapi import FastAPI

from src.core.config import get_config
from src.service.proxy import Proxy
from src.service.bot import Bot

app = FastAPI(
    title="Youtube Bot Service",
    version='0.0.1',
)

config = get_config()


@app.get("/")
def read_root():
    logger.info(config.live_ids)
    bot = Bot(config.live_ids)
    bot.test()
    return {"Hello": "World"}


if __name__ == "__main__":
    pass