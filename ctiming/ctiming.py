"""
ID: araoudu1
LANG: PYTHON3
TASK: ctiming
"""


# Find the total amount minutes per day.
def find_total_mins(d, h, m): return (d * 24 * 60) + (h * 60) + m


with open('ctiming.in') as f:
    d, h, m = [int(number) for number in f.read().split()]


def solve():
    with open('ctiming.out', 'w') as f:
        # If it was too early
        if find_total_mins(11, 11, 11) > find_total_mins(d, h, m):
            f.write('-1\n')
        else:
            f.write(f'{find_total_mins(d, h, m) - find_total_mins(11, 11, 11)}\n')


solve()
