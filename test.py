import os


def test_milk2():
    with open('milk2.in', 'w') as f:
        f.write("""10
                2 3
                4 5
                6 7
                8 9
                10 11
                12 13
                14 15
                16 17
                18 19
                1 20""")

    __import__('milk2.milk2')

    f = open('milk2.out')
    assert (f.read() == "19 0\n")
    f.close()

    os.remove('milk2.in')
    os.remove('milk2.out')
