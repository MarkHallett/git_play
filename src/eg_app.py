# eg_app.py

import sys

from devtools import debug


def b_002b():
    # comment
    x = 10
    return x


def branch2():
    # main branch 2 dev work etc
    x = 20
    return x


def branch3():
    # comment
    x = 10
    return x

def branch5():
    # comment
    x = 10
    return x

if __name__ == '__main__':
    print('x-xxxxyyyyyyy---------------------x')
    print(__file__)
    print(sys.version)
    print(sys.executable)
    branch2()
    branch3()
    branch4()
