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

    def delete(self):
        pass

    def read(self):
        pass

    def change_status(self):
        pass
