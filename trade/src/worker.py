from typing import Optional

from .enum import State


class Worker:

    def __init__(self):
        pass

    def run(self) -> None:
        state = None
        while True:
            state = None

    def _worker(self, old_state: Optional[State]) -> State:
