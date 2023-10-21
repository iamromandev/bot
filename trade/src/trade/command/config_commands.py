from typing import List, Dict, Any
from pathlib import Path

from loguru import logger
from questionary import Separator, prompt

from trade.util import render_template


def ask_user_overwrite(path: Path) -> bool:
    questions: List[Dict[str, Any]] = [
        {
            "type": "confirm",
            "name": "overwrite",
            "message": f"File {path} already exists. Overwrite?",
            "default": False
        }
    ]
    answers = prompt(questions)
    return answers.get("overwrite", False)


def ask_user_config() -> Dict[str, Any]:
    questions: List[Dict[str, Any]] = [
        {
            "type": "confirm",
            "name": "dry_run",
            "message": "Do you want to enable Dry-run (simulated trades)?",
            "default": True,
        },
        {
            "type": "select",
            "name": "exchange_name",
            "message": "Select exchange",
            "choices": [
                "binance",
                Separator("------------------"),
                "other",
            ],
        },
        {
            "type": "confirm",
            "name": "trading_mode",
            "message": "Do you want to trade Perpetual Swaps (perpetual futures)?",
            "default": False,
            "filter": lambda val: "futures" if val else "spot",
            "when": lambda x: x["exchange_name"] in ["binance", "gate", "okx"],
        }
    ]

    answers = prompt(questions)
    answers["trading_mode"] = answers.get("trading_mode", "spot")

    return answers


def create_new_config(config_path: Path, selections: Dict[str, Any]) -> None:
    from jinja2.exceptions import TemplateNotFound

    try:
        template = selections.get("exchange_name")
        selections["exchange"] = render_template(
            template=f"exchanges/{template}.j2",
            arguments=selections
        )
    except TemplateNotFound:
        selections["exchange"] = render_template(
            template=f"exchanges/generic.j2",
            arguments=selections
        )

    config_text = render_template(
        template='base_config.json.j2',
        arguments=selections
    )

    logger.info(f"Writing config to `{config_path}`.")
    logger.info("Please make sure to check the configuration contents and adjust settings to your needs.")

    config_path.write_text(config_text)


def start_new_config(args: Dict[str, Any]) -> None:
    config_path = Path(args.get("config")[0])
    logger.info(f"Config Path {str(config_path)}")
    if config_path.exists():
        overwrite = ask_user_overwrite(config_path)
        if overwrite:
            config_path.unlink()

    selections = ask_user_config()
    create_new_config(config_path, selections)
