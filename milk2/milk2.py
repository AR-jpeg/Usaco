"""
ID: araoudu1
LANG: PYTHON3
TASK: milk2
"""


from typing import List


class IntervalPeriod():
    def __init__(self, low: int, high: int) -> None:
        self._low: int = low
        self._high: int = high

    def getLow(self) -> int:
        return self._low

    def getHigh(self) -> int:
        return self._high

    def __repr__(self) -> str:
        return f"<Interval Period start:{self._low} end:{self._high}>"

    def __lt__(self, other):
        return self._low < other.getLow()


with open('milk2.in') as f:
    lines = f.readlines()

    N = int(lines[0])
    lines = lines[1:]

intervals: List[IntervalPeriod] = []

# Preprocces the data
for i, item in enumerate(lines):
    lines[i] = item.strip('\n').split()
    intervals.append(IntervalPeriod(int(lines[i][0]), int(lines[i][1])))

intervals = sorted(intervals)

low: int = intervals[0].getLow()
high: int = intervals[0].getHigh()
maxInterval: int = high-low
maxGap: int = 0

for i, interval in enumerate(intervals):
    if (interval.getLow() <= high):
        high = max(interval.getHigh(), high)
    else:
        maxInterval = max(maxInterval, high-low)
        maxGap = max(maxGap, interval.getLow()-high)
        low = interval.getLow()
        high = interval.getHigh()


with open('milk2.out', 'w') as f:
    f.write(str(maxInterval) + " " + str(maxGap) + '\n')
