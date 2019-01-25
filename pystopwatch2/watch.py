import threading
import time

from enum import Enum
from collections import defaultdict

tag_default = '__default1958__'
th_lock = threading.Lock()


class ClockState(Enum):
    PAUSE = 0
    RUN = 1


class Clock:
    def __init__(self):
        self.prev_time = time.time()
        self.sum = 0.
        self.state = ClockState.PAUSE

    def __str__(self):
        return 'state=%s elapsed=%.4f prev_time=%.8f' % (self.state, self.sum, self.prev_time)

    def __repr__(self):
        return self.__str__()


class PyStopwatch:
    def __init__(self):
        self.clocks = defaultdict(lambda: Clock())

    def start(self, tag=None):
        if tag is None:
            tag = tag_default
        with th_lock:
            clock = self.clocks[tag]
            if clock.state == ClockState.RUN:
                return
            clock.state = ClockState.RUN
            clock.prev_time = time.time()

    def pause(self, tag=None):
        if tag is None:
            tag = tag_default
        with th_lock:
            clock = self.clocks[tag]
            clock.state = ClockState.PAUSE
            clock.sum += time.time() - clock.prev_time

    def clear(self, tag=None):
        if tag is None:
            tag = tag_default
        del self.clocks[tag]

    def get_elapsed(self, tag=None):
        if tag is None:
            tag = tag_default
        clock = self.clocks[tag]
        elapsed = clock.sum
        if clock.state == ClockState.RUN:
            elapsed += time.time() - clock.prev_time

        return elapsed

    def keys(self):
        return self.clocks.keys()

    def __str__(self):
        return '\n'.join(['%s: %s' % (k, v) for k, v in self.clocks.items()])

    def __repr__(self):
        return self.__str__()
