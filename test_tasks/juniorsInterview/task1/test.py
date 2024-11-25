import unittest

from solution import strict


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


class TestStrictDecorator(unittest.TestCase):
    """Проверяем функцию sum_two"""

    def test_valid_arguments(self):
        """Проверка на корректный вывод"""
        self.assertEqual(sum_two(1, 2), 3)

    def test_invalid_argument_type_float(self):
        """Соответствие аргументов типам данных (float)"""
        with self.assertRaises(TypeError) as context:
            sum_two(1, 2.4)  # Ожидается исключение TypeError
        self.assertEqual(
            str(context.exception),
            f"Переданы неверные аргументы в функцию sum_two",
        )

    def test_invalid_argument_type_string(self):
        """Соответствие аргументов типам данных (str)"""
        with self.assertRaises(TypeError) as context:
            sum_two(1, "two")
        self.assertEqual(
            str(context.exception),
            f"Переданы неверные аргументы в функцию sum_two",
        )

    def test_invalid_argument_count(self):
        """Передано нужное количество аргументов"""
        with self.assertRaises(TypeError) as context:
            sum_two(1)
        self.assertEqual(
            str(context.exception),
            "sum_two() missing 1 required positional argument: 'b'",
        )

    def test_extra_arguments(self):
        """Проверяется на лишний аргумент"""
        with self.assertRaises(TypeError) as context:
            sum_two(1, 2, 3)  # Ожидается исключение TypeError из-за лишнего аргумента
        self.assertEqual(
            str(context.exception),
            "sum_two() takes 2 positional arguments but 3 were given",
        )


if __name__ == "__main__":
    unittest.main(verbosity=True)
