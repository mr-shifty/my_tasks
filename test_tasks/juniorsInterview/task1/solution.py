from inspect import signature


def strict(func):
    def wrapper(*args, **kwargs):
        sig = signature(func)
        if all(
            map(
                lambda x, y: isinstance(*(x, y.annotation)),
                args,
                [param for param in sig.parameters.values()],
            )
        ):
            return func(*args, **kwargs)
        raise TypeError(f"Переданы неверные аргументы в функцию {func.__name__}")

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print(sum_two(1, 2))  # >>> 3
    print(sum_two(1, 2.4))  # >>> TypeError
