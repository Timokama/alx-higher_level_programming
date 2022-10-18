#!/usr/bin/python3
"""Program to compute solutions to the 'N Queens' problem.

The 'N Queens' problem is to enumerate all the possible arrangements
of N Queens on an NxN chessboard such that no two pieces lie along
the same vertical, horizontal, or diagonal. It is difficult to compute
by brute force because even for relatively small `n` the number of
arrangements to test grows factorially (N**2 choose N). The solution
uses backtracking to quickly prune the tree of possible arrangments by
abandoning unsuccessful branches once a partial solution can be rejected.

Example:
    This program can be invoked from the command line by specifying the
        value for `n`, such as:

            $ ./nqueens 8
"""
def nqueens(n, c=[]):
    if reject(n, c):
        return
    if accept(n, c):
        print(c)
    s = first_candidate(n, c)
    while s is not None:
        nqueens(n, s)
        s = next_candidate(n, s)

def reject(n, c):
    try:
        last = c[-1]
    except IndexError:
        return False
    for i in c[:-1]:
        if i[0] == last[0] or i[1] == last[1]:
            return True
        if abs(last[0] - i[0]) == abs(last[1] - i[1]):
            return True
    return False

def accept(n, c):
    if len(c) == n:
        return True
    return False

def first_candidate(n, c):
    if len(c) == n:
        return None
    try:
        last = c[-1]
    except IndexError:
        return [[0, 0]]
    if last[1] < n-1:
        return c + [[last[0], last[1]+1]]
    elif last[0] < n-1:
        return c + [[last[0]+1, 0]]
    else:
        return None

def next_candidate(n, s):
    last = s[-1]
    if last[1] < n-1:
        return s[:-1] + [[last[0], last[1]+1]]
    elif last[0] < n-1:
        return s[:-1] + [[last[0]+1, 0]]
    else:
        return None

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    n = sys.argv[1]
    if not n.isdigit():
        print('N must be a number')
        exit(1)
    n = int(n)
    if n < 4:
        print('N must be at least 4')
        exit(1)
        nqueens(n)
        exit(0)
