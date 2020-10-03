"""Solve the sqare pasture problem from usaco."""


def solve():
    """
    The arguements come in like:
        p1: [(1,8), (5,9)]
        p2: [(6,6), (8,8)]
    """
    pastures = []

    with open('square.in') as f:
        data = f.readlines()
        for index, line in enumerate(data):
            pastures.append([])

            for x in line.split(' '):
                pastures[index].append(int(x))

        # print(pastures)

    pasture_1 = pastures[0]
    pasture_2 = pastures[1]

    print(pasture_1, pasture_2)

    # First find the right-most point
    p1_right = pasture_1[2]
    p2_right = pasture_2[2]

    # Then find the left-most point
    p1_left = pasture_1[0]
    p2_left = pasture_2[0]

    # Get the total x that is needed...
    total_x_needed = max(p1_right, p2_right) - min(p1_left, p2_left)

    # Do the same steps for y
    p1_top = pasture_1[3]
    p2_top = pasture_2[3]

    p1_bottom = pasture_1[1]
    p2_bottom = pasture_2[1]

    total_y_needed = max(p1_top, p2_top) - min(p1_bottom, p2_bottom)

    # Finnaly, to solve the problem, just take the bigger of x/y and square
    with open('square.out', 'w') as f:
        f.write(str(max(total_x_needed, total_y_needed) ** 2))
        f.write('\n')
    return max(total_x_needed, total_y_needed) ** 2


solve()
