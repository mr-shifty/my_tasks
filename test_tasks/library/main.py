import os

from handler import Library
from rich import print

library = Library()


def main():
    print(
        """
            1. Добавить книгу,
            2. Удалить книгу,
            3. Отобразить все книги,
            4. Изменить статус книги
            q. Выход
            """
    )
    # try:

    match input("Введите число для выбора (1-4) или q для выхода "):
        case "1":
            (
                library.update()
                if os.path.exists("data.json")
                else library.create()
            )
        case "2":
            library.delete()
        case "3":
            library.read()
        case "4":
            library.change_status()
        case "q":
            exit()
        case _:
            print("Введите число от 1 до 4 или q для выхода")
            main()
    (main() if input("Продолжить - Enter, q - выход ") != "q" else exit())

    # except ValueError:
    #     print("Дурак? Сказали же число ввести")
    #     main()


if __name__ == "__main__":
    main()
