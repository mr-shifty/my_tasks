from rich import print

from test_tasks.library.hendler import Library
from test_tasks.library.test_info import books

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
    try:
        choice = int(input("Введите число для выбора (1-5) "))
        match choice:
            case 1:
                library.create(books)
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                exit()
            case _:
                print("Введите число от 1 до 4 или проваливайте")
                main()
    except ValueError:
        print("Дурак? Сказали же число ввести")
        main()


if __name__ == "__main__":
    main()
