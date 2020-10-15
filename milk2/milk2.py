"""
ID: araoudu1
LANG: PYTHON3
TASK: milk2
"""


from typing import List


class IntervalPeriod():
    """Represent an interval period."""

    def __init__(self, low_start: int, high_end: int) -> None:
        self._low: int = low_start
        self._high: int = high_end

    def get_low(self) -> int:
        "Return the interval's low period."
        return self._low

    def get_high(self) -> int:
        """Return the interval's high period."""
        return self._high

    def __repr__(self) -> str:
        return f"<Interval Period start:{self._low} end:{self._high}>"

    def __lt__(self, other):
        return self._low < other.get_low()


with open('milk2.in') as f:
    lines: List = f.readlines()

    N = int(lines[0])
    lines = lines[1:]

intervals: List[IntervalPeriod] = []

# Preprocces the data
for i, item in enumerate(lines):
    lines[i] = item.strip('\n').split()
    intervals.append(IntervalPeriod(int(lines[i][0]), int(lines[i][1])))

intervals = sorted(intervals)

low: int = intervals[0].get_low()
high: int = intervals[0].get_high()
maxInterval: int = high-low
maxGap: int = 0

for i, interval in enumerate(intervals):
    if interval.get_low() <= high:
        high = max(interval.get_high(), high)
    else:
        maxInterval = max(maxInterval, high-low)
        maxGap = max(maxGap, interval.get_low()-high)
        low = interval.get_low()
        high = interval.get_high()


with open('milk2.out', 'w') as f:
    f.write(str(maxInterval) + " " + str(maxGap) + '\n')
