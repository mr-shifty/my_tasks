import pretty_errors
from rich import print


def bubble_sort(data):
    for _ in range(len(data) - 1):
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]

    return data


if __name__ == "__main__":
    print(*bubble_sort([5, 1, 22, 5, -54, 12, 100, -12, 7, 83]))
