"""
ID: araoudu1
LANG: PYTHON3
TASK: ride
"""


def solve():
    with open('ride.in') as f:
        data = f.readlines()

        group_name = data[0].strip()
        commet_name = data[1].strip()

    group_id = 1
    commet_id = 1

    for letter in group_name:
        group_id *= (ord(letter) - 64)

    for letter in commet_name:
        commet_id *= (ord(letter) - 64)

    with open('ride.out', 'w') as f:
        if group_id % 47 == commet_id % 47:
            f.write('GO')
        else:
            f.write('STAY')
        f.write('\n')


solve()
