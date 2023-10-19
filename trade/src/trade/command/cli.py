from typing import Dict

from trade import __version__, constants


class Arg:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


OPTIONS: Dict[str, Arg] = {
    # common options
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
    "logfile": Arg(
        "--logfile", "--log-file",
        help="Log to the file specified. Special values are: 'syslog', 'journald'. "
             "See the documentation for more details.",
        metavar="FILE",
    ),
    "config": Arg(
        "-c", "--config",
        help=f"Specify configuration file (default: `datadir/{constants.DEFAULT_CONFIG}` "
             f"or `config.json` whichever exists). "
             f"Multiple --config options may be used. "
             f"Can be set to `-` to read config from stdin.",
        action="append",
        metavar="PATH",
    ),
    "datadir": Arg(
        "-d", "--datadir", "--data-dir",
        help="Path to directory with all data.",
        metavar="PATH",
    ),

    # strategy options
    "strategy": Arg(
        "-s", "--strategy",
        help="Specify strategy class name which will be used by the bot.",
        metavar="NAME",
    ),

    # start trade
    "dry_run": Arg(
        '--dry-run',
        help='Enforce dry-run for trading (removes Exchange secrets and simulates trades).',
        action='store_true',
    ),
}
