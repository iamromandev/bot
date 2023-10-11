import sys

from typing import Optional, List, Any

from loguru import logger

from trade import __version__
from trade.command import Arguments


def main(sysargv: Optional[List[str]] = None) -> None:
    # import argparse
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-n", "--name", required=True)
    # args = parser.parse_args()
    # print(f'Hi {args.name} , Welcome ')

    return_code: Any = 1
    try:
        arguments = Arguments(sysargv)
        args = arguments.parsed_args
        logger.info(f"Args: {args}")

        # call sub commands
        if "func" in args:
            logger.info(f"trade {__version__}")
            return_code = args["func"](args)

    except Exception as e:
        logger.error(str(e))
        logger.exception("Fatal exception!")
    finally:
        sys.exit(return_code)


if __name__ == '__main__':  # pragma: no cover
    main()
