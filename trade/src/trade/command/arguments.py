import argparse

from typing import Optional, List, Dict, Any

from trade.command.cli import OPTIONS

ARGS_COMMON = ["verbosity", "version", "logfile", "config", "datadir"]
ARGS_STRATEGY = ["strategy"]
ARGS_START = ["dry_run"]
ARGS_DATA_DIR = ["datadir"]


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
        common_group = common_parser.add_argument_group("Common Arguments")
        self._build_arguments(parser=common_group, options=ARGS_COMMON)

        # strategy parser
        strategy_parser = argparse.ArgumentParser(add_help=False)
        strategy_group = common_parser.add_argument_group("Strategy Arguments")
        self._build_arguments(parser=strategy_group, options=ARGS_STRATEGY)

        # main parser
        self.parser = argparse.ArgumentParser(description="Crypto Trading Bot")
        self._build_arguments(parser=self.parser, options=["version"])

        # sub parsers
        sub_parsers = self.parser.add_subparsers(dest="command")

        # start subcommand
        from trade.command import (
            start_trade,
            create_datadir
        )
        start_subcommand = sub_parsers.add_parser(
            "start",
            help="Start Trade Module.",
            parents=[common_parser, strategy_parser]
        )
        start_subcommand.set_defaults(func=start_trade)
        self._build_arguments(parser=start_subcommand, options=ARGS_START)

        # data dir subcommand
        datadir_subcommand = sub_parsers.add_parser(
            "create-datadir",
            help="Create Data Directory."
        )
        datadir_subcommand.set_defaults(func=create_datadir)
        self._build_arguments(parser=datadir_subcommand, options=ARGS_DATA_DIR)

