import json

import regex
from loguru import logger
from nested_lookup import nested_lookup

JSON_REGEX = r'\{(?:[^{}]|(?R))*\}'


def to_camel(string: str) -> str:
    res = "".join(word.capitalize() for word in string.split("_"))
    return res[0].lower() + res[1:]


def find_jsons(text: str) -> list:
    pattern = regex.compile(JSON_REGEX)
    return pattern.findall(text)


def find_single_item(key: str, data: str | list | dict) -> str | None:

    if isinstance(data, list):
        copy = []
        for item in data:
            try:
                item = json.loads(item)
                copy.append(item)
                logger.info(item)
            except:
                pass
        data = copy

    items = nested_lookup(key, data)
    return items[0] if len(items) > 0 else None
