import json

import regex
from loguru import logger
from nested_lookup import nested_lookup
from furl import furl

JSON_REGEX = r"\{(?:[^{}]|(?R))*\}"


def to_camel(string: str) -> str:
    res = "".join(word.capitalize() for word in string.split("_"))
    return res[0].lower() + res[1:]


def find_jsons(data: str) -> list:
    pattern = regex.compile(JSON_REGEX)
    return pattern.findall(data)


def find_single_item(data: str | list | dict, key: str) -> str | None:
    if isinstance(data, list):
        copy = []
        for item in data:
            try:
                item = json.loads(item)
                copy.append(item)
            except:
                pass
        data = copy

    items = nested_lookup(key, data)
    return items[0] if len(items) > 0 else None


def find_args_from_url(url: str, params: tuple) -> dict:
    f = furl(url)
    args = {
        param: f.args[param]
        for param in params
    }
    return args
