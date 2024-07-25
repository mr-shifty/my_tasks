import re


def check_year(year: str) -> str:
    while True:
        if re.fullmatch(r"(?!0)\d{4}", str(year)):
            return year
        year = input(
            "Неверный формат, год дожен быть четырехзначным числом от 1: "
        )


def find_match(pattern: str, data: str) -> bool:
    return bool(re.findall(rf"(?i)[{pattern}]{{2,}}", str(data)))
