import sys

from typing import Optional, List, Any

from trade.command import Arguments


def main(sysargv: Optional[List[str]] = None) -> None:
    # import argparse
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-n", "--name", required=True)
    # args = parser.parse_args()
    # print(f'Hi {args.name} , Welcome ')

    return_code: Any = 1
    try:
        print("Lal Lal")
        print(sysargv)

        arguments = Arguments(sysargv)
        args = arguments.parsed_args
        print(args)
    except Exception:
        pass
    finally:
        sys.exit(1)
    pass


if __name__ == '__main__':  # pragma: no cover
    main()
