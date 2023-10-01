from enum import Enum


class State(Enum):
    # bot states
    RUNNING = 1
    STOPPED = 2
    RECONFIG = 3

    def __str__(self):
        return self.name.lower()
