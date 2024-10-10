import pretty_errors
from rich import print

from features.decorators import execute_time


@execute_time()
def pascal():
    n = 7
    lst = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j != 0 and j != i:
                row[j] = lst[i - 1][j - 1] + lst[i - 1][j]
        lst.append(row)

    for k in lst:
        print(k)


if __name__ == "__main__":
    pascal()
