from functools import reduce

# from rich import print

cache = {}


def factorial(n: int) -> int | str:
    """Выводит результат или значение из кэша"""
    global cache
    key = f"factorial({n})"

    def check_res() -> bool:
        """Проверяет нахождение результата в кэше"""
        return key in cache

    def calculate_factorial() -> int:
        """Вычисляет факториал числа"""
        if n == 1:
            cache[1] = f"factorial({1})"
            return 1
        cache[key] = reduce(lambda x, y: x * y, range(1, n + 1))
        return cache.get(key)

    if check_res():
        print(f"Get from cache value {key}")
        return cache.get(key)
    return calculate_factorial()


print(factorial(5))
print(factorial(6))
print(factorial(5))
print(cache)
