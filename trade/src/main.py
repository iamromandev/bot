from typing import Optional, List

from loguru import logger

def main(sysargv: Optional[List[str]]) -> None:

    logger.debug(f"Main Args: {sysargv}")

    return None
