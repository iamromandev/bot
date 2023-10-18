from pathlib import Path
from loguru import logger


def create_dir(directory: str, create: bool = True) -> Path:
    sub_dirs = [
        "logs"
    ]
    folder = Path(directory)
    if not folder.is_dir():
        if create:
            folder.mkdir(parents=True)
            logger.info(f"Created data directory: {folder}")

    for sub_dir in sub_dirs:
        sub_folder = folder / sub_dir
        if not sub_folder.is_dir():
            sub_folder.mkdir(parents=False)

    return folder
