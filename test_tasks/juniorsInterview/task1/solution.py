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
