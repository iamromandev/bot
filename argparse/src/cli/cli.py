import argparse
import time

import arrow


def greet(tz, repeat=1, interval=3):
    """Parse a timezone and greet a location a number of times."""
    for i in range(repeat):
        if i > 0:  # no delay needed on first round
            time.sleep(interval)
        now = arrow.now(tz)
        friendly_time = now.format("h:mm a")
        seconds = now.format("s")
        location = tz.split("/")[-1].replace("_", " ")
        print(f"Hello, {location}!")
        print(f"The time is {friendly_time} and {seconds} seconds.\n")


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("tz", help="The timezone")
    parser.add_argument(
        "-r",
        "--repeat",
        help="number of times to repeat the greeting",
        default=1,
        type=int,
    )
    parser.add_argument(
        "-i",
        "--interval",
        help="time in seconds between iterations",
        default=3,
        type=int,
    )
    args = parser.parse_args()
    greet(args.tz, args.repeat, args.interval)
