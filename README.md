# pystopwatch
Multi-functional Simple Stopwatch for Python.

- Multiple Stopwatch by Tags
- Manage elapsed times by tags
- Example of use : profiling python codes(latency by functions, ...)

## Install

```
$ pip install pystopwatch2
```

## Usage

```python
from pystopwatch2 import PyStopwatch

w = PyStopwatch()
w.start(tag='a')
time.sleep(1)
w.pause('a')
e = w.get_elapsed('a')
print(e)
# 1.0xxx

w.start(tag='b')
time.sleep(0.5)
w.pause('b')
print(w)

"""
a: state=ClockState.PAUSE elapsed=1.0027 prev_time=1548382910.66398311
b: state=ClockState.PAUSE elapsed=0.5051 prev_time=1548382911.66670585
"""

e.clear('a')
e.clear('b')
```
