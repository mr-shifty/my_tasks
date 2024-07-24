import re


def check_year(year: str):
    while True:
        if re.fullmatch(r"(?!0)\d{4}", str(year)):
            return year
        year = input(
            "Неверный формат, год дожен быть четырехзначным числом от 1: "
        )


if __name__ == "__main":
    check_year("1234")
