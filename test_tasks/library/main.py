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
        """
    )
    try:
        int(input("Введите число для выбора: "))
        library.create(books)
    except ValueError:
        print("Дурак? Сказали же число ввести")
        main()


if __name__ == "__main__":
    main()
