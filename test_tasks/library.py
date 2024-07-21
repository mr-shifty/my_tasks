from rich import print

books = [
    {
        "id": 1,
        "title": "hui",
        "author": "Her Mayor",
        "year": 1984,
        "status": "В наличии",
    },
    {
        "id": 2,
        "title": "bla",
        "author": "Bla Bla",
        "year": 1488,
        "status": "Нет в наличии",
    },
]


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
                self.id: len(lst) + 1,
                self.title: input("Введите название книги: "),
                self.author: input("Введите автора: "),
                self.year: int(input("Введите год: ")),
                self.status: "В наличии",
            },
        )
        print(lst)
        return lst

    def delete(self, lst):
        pass

    def read(self):
        pass

    def change_status(self):
        pass


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
