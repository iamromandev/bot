import shutil

from pathlib import Path

from loguru import logger

from trade import constants


def create_dir(directory: str, create: bool = True) -> Path:
    sub_dirs = [
        "logs",
        constants.DIR_STRATEGIES,
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


def copy_files(directory: Path, overwrite: bool = False) -> None:
    if not directory.is_dir():
        return None

    source_dir = Path(__file__).parents[1] / "templates"

    for source, target in constants.DATA_FILES.items():
        target_dir = directory / target
        if not target_dir.is_dir():
            return False

        target_file = target_dir / source
        if target_file.exists():
            if not overwrite:
                continue

        shutil.copy(str(source_dir / source), str(target_file))
