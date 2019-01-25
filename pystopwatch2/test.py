import time
import unittest

from pystopwatch2.watch import PyStopwatch


class TestStringMethods(unittest.TestCase):

    def test_stopwatch(self):
        w = PyStopwatch()
        w.start('a')
        time.sleep(1)
        w.pause('a')
        e = w.get_elapsed('a')
        self.assertAlmostEqual(1.0, e, delta=0.05)

        w.start('b')
        time.sleep(0.5)
        w.pause('b')
        e_a = w.get_elapsed('a')
        e_b = w.get_elapsed('b')
        self.assertAlmostEqual(1.0, e_a, delta=0.05)
        self.assertAlmostEqual(0.5, e_b, delta=0.05)

        print(w.__repr__())

    def test_running_stopwatches(self):
        w = PyStopwatch()
        for i in range(5):
            key = 'key_%d' % i
            w.start(key)
            time.sleep(0.1)

        for i in range(5):
            key = 'key_%d' % i
            e = w.get_elapsed(key)
            self.assertAlmostEqual((5 - i) * 0.1, e, delta=0.03)


if __name__ == '__main__':
    unittest.main()
