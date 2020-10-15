"""
ID: araoudu1
LANG: PYTHON3
TASK: beads
"""

from typing import List, Any


with open('beads.in', 'r') as fin:
    N = int(fin.readline())
    beads: str = fin.readline()[:-1]


def canCollectBead(s: List[Any]) -> bool:
    """See if we can collect a bead.

    Args:
        s: The bead
    Returns:
        bool: Weather we can collect the bead.  
    """
    return not ('r' in s and 'b' in s)


beads *= 3  # So that we can wraparound the necklace
max: int = 0  # The total result

for p in range(N, N*2):    # Loop through the 2nd bead string (so you can use
    i: int = p-1             # wraparounds for the front and back)
    left: List[str] = []
    # The same logic as the other solution
    while i > 0:
        if canCollectBead(left + [beads[i]]):
            left.append(beads[i])
            i -= 1
        else:
            break

    # Make sure there are no duplicate beads (see line 23)
    i = p
    right: List[str] = []
    # Same logic
    while i < 3*N - 1:
        if canCollectBead(right + [beads[i]]):
            right.append(beads[i])
            i += 1
        else:
            break

    result = len(left) + len(right)
    if result >= N:
        max = N
        break
    elif result > max:
        max = result

with open('beads.out', 'w') as f:
    f.write(str(max) + "\n")
