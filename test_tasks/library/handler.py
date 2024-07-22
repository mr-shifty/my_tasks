import json
import time


class Library:
    def __init__(self) -> None:
        self.id = int(time.time() * 1000)
        self.data = "data.json"
        self.title = "title"
        self.author = "author"
        self.year = "year"
        self.status = "status"

    def create(self):
        with open("data.json", "w", encoding="utf-8") as file:

            dct = {
                input("Введите автора: "): {
                    self.id: {
                        self.title: input("Введите название книги: "),
                        self.year: int(input("Введите год: ")),
                        self.status: "В наличии",
                    },
                },
            }
            return json.dump(dct, file, ensure_ascii=False, indent=2)

    def update(self):
        with open(self.data, encoding="utf-8") as file:
            self.id = int(time.time() * 1000)
            data = json.load(file)
            self.author = input("Введите автора: ")
            if self.author not in data:
                data.update(
                    {
                        self.author: {
                            self.id: {
                                self.title: input("Введите название книги: "),
                                self.year: int(input("Введите год: ")),
                                self.status: "В наличии",
                            },
                        },
                    },
                )
            else:
                data[self.author][self.id] = {
                    self.title: input("Введите название книги: "),
                    self.year: int(input("Введите год: ")),
                    self.status: "В наличии",
                }

        with open(self.data, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def delete(self):
        # with open(self.data, encoding="utf-8") as file:
        #     data = json.load(file)
        #     remove_id = int(input())
        #     for
        pass

    def read(self):
        with open(self.data, encoding="utf=8") as file:
            data = json.load(file)
            for key, value in data.items():
                print(f"\nid={key}: {value}")

    def change_status(self):
        pass
