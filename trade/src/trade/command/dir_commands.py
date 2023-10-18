from typing import Dict, Any

from loguru import logger

from trade.config.dir_ops import (
    create_dir
)


def create_datadir(args: Dict[str, Any]) -> None:

    data_dir = args.get("datadir", None)

    logger.info(f"Creating Data Directory... {data_dir}")

    if data_dir:
        dir = create_dir(data_dir, create=True)
