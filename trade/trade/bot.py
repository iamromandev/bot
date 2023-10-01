from enum import (
    State,
)


class Bot:

    def __init__(self):
        self.__state = State.STOPPED

