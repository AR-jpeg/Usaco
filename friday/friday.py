"""
ID: araoudu1
LANG: PYTHON3
TASK: friday
"""


def isLeapYear(year: int) -> bool:
    if (year % 100 == 0) and year % 400 == 0:
        return True
    elif (year % 4 == 0) and (year % 100):
        return True
    else:
        return False


def solve():
    with open('friday.in') as f:
        years = int(f.read())

    freq = [0, 0, 0, 0, 0, 0, 0]
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leapMonths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 2

    for i in range(1900, 1900+years):
        if isLeapYear(i):
            for month in range(12):
                for d in range(leapMonths[month]):
                    if day >= 7:
                        day = 0
                    if d == 12:
                        freq[day] += 1
                    day += 1
        else:
            for month in range(12):
                for d in range(months[month]):
                    # print(day)
                    if day >= 7:
                        day = 0
                    if d == 12:
                        freq[day] += 1
                    day += 1

    with open('friday.out', 'w') as file:
        for i, f in enumerate(freq):
            if i == 6:
                file.write(str(f))
            else:
                file.write(str(f) + ' ')

        file.write('\n')


solve()
