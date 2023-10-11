from typing import Dict

from trade import __version__


class Arg:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


OPTIONS: Dict[str, Arg] = {
    "verbosity": Arg(
        "-v", "--verbose",
        help="Verbose mode (-vv for more, -vvv to get all messages).",
        action="count",
        default=0,
    ),
    "version": Arg(
        "-V", "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    ),
    # start trade
    "dry_run": Arg(
        '--dry-run',
        help='Enforce dry-run for trading (removes Exchange secrets and simulates trades).',
        action='store_true',
    ),
}
