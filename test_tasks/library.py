from rich import print

book = [
    {
        "id": 1,
        "title": "hui",
        "author": "Her Mayor",
        "year": 1984,
        "status": "В наличии",
    },
]


def create(lst):
    lst.append(
        {
            "id": 2,
            "title": input("Введите название книги: "),
            "author": input("Введите автора: "),
            "year": int(input("Введите год: ")),
            "status": "В наличии",
        },
    )
    print(lst)
    return lst


class Library:
    def __init__(self) -> None:
        self.id = "id"
        self.title = "title"
        self.author = "author"
        self.year = "year"
        self.status = "status"

    def create(self, lst):
        lst.append(
            {
                self.id: 2,
                self.title: input("Введите название книги: "),
                self.author: input("Введите автора: "),
                self.year: int(input("Введите год: ")),
                self.status: "В наличии",
            },
        )
        print(lst)
        return lst

    def delete(self):
        pass

    def read(self):
        pass

    def change_status(self):
        pass


def main():
    print(
        """
        1. Добавить книгу,
        2. Удалить книгу,
        3. Отобразить все книги,
        4. Изменить статус книги\t
        """
    )
    try:
        int(input("Введите число для выбора: "))
        library = Library()
        library.create(book)
    except ValueError:
        print("Дурак? Сказали же число ввести")
        main()


if __name__ == "__main__":
    main()
