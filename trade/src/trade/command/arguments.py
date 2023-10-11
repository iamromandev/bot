import argparse

from typing import Optional, List, Dict, Any

from .cli import OPTIONS

ARGS_COMMON = ["verbosity", "version"]


class Arguments:
    def __init__(self, args: Optional[List[str]]) -> None:
        self.args = args
        self._parsed_args: Optional[argparse.Namespace] = None

    @property
    def parsed_args(self) -> Dict[str, Any]:
        if not self._parsed_args:
            self._build_commands()
            self._parsed_args = self._parse_arguments()
        return vars(self._parsed_args)

    def _parse_arguments(self) -> argparse.Namespace:
        parsed_args = self.parser.parse_args(self.args)
        return parsed_args

    def _build_arguments(self, parser, options):
        for option in options:
            opt = OPTIONS.get(option)
            parser.add_argument(*opt.args, dest=option, **opt.kwargs)

    def _build_commands(self) -> None:

        # common parser
        common_parser = argparse.ArgumentParser(add_help=False)
        group = common_parser.add_argument_group("Common Arguments")
        self._build_arguments(parser=group, options=ARGS_COMMON)

        # main parser
        self.parser = argparse.ArgumentParser(description="Crypto Trading Bot")
        self._build_arguments(parser=self.parser, options=["version"])