from features import execute_time


@execute_time()
def get_nod_slow(a: int, b: int) -> int:
    """
    Находит Наибольший Общий Делитель.
    Стандартный способ. Медлeный алгоритм.
    """

    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@execute_time(limit=1)
def get_nod_fast(a: int, b: int) -> int:
    """
    Находит Наибольший Общий Делитель.
    Стандартный способ. Быстрый Алгоритм.
    """
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


# @execute_time()
def get_nod_rec(a: int, b: int) -> int:
    """
    Находит Наибольший Общий Делитель.
    Рекурсия."""

    if b == 0:
        return a

    return get_nod_rec(b, a % b)


if __name__ == "__main__":
    print(get_nod_slow(15, 1210501983))
    print(get_nod_fast(15, 1210501983))

    print(get_nod_rec(15, 121050))
