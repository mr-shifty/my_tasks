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
            5. Выход
            """
    )
    # try:

    match int(input("Введите число для выбора (1-5) ")):
        case 1:
            (
                library.update()
                if os.path.exists("data.json")
                else library.create()
            )
        case 2:
            pass
        case 3:
            library.read()
        case 4:
            pass
        case 5:
            exit()
        case _:
            print("Введите число от 1 до 5 или проваливайте")
            main()
    main() if input("Выполнить еще? ") == "y" else exit()

    # except ValueError:
    #     print("Дурак? Сказали же число ввести")
    #     main()


if __name__ == "__main__":
    main()
