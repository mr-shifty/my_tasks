import json
import time


class Library:
    def __init__(self) -> None:
        self.id = int(time.time() * 1000)
        self.data = "data.json"
        self.title = "Название книги"
        self.author = "Автор"
        self.year = "Год издания"
        self.status = "Статус книги"

    def create(self):
        with open("data.json", "w", encoding="utf-8", errors="ignore") as file:

            dct = {
                input("Введите автора: "): {
                    self.id: {
                        self.title: input("Введите название книги: "),
                        self.year: int(input("Введите год: ")),
                        self.status: "В наличии",
                    },
                },
            }
            json.dump(dct, file, indent=2)
        print("Книга успешно добавлена")

    def update(self):
        with open(self.data, encoding="utf-8", errors="ignore") as file:
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
        print("Книга успешно добавлена")

        with open(self.data, "w", encoding="utf-8", errors="ignore") as file:
            json.dump(data, file, indent=2)

    def read(self):
        try:
            with open(self.data, encoding="utf=8") as file:
                data = json.load(file)
                flag = False
                all_count = 0
                for key, value in data.items():
                    if value:
                        flag = True
                        print(
                            f"\nАвтор: {key} ({len(value.values())} шт.)\n"
                            f"Книги:"
                        )
                        for k, v in value.items():
                            print(
                                f"\tid: {k}\n"
                                f"\tНазвание: {v[self.title]}\n"
                                f"\tГод издания: {v[self.year]}\n"
                                f"\tСтатус: {v[self.status]}\n"
                            )
                            all_count += 1
                if flag:
                    print(f"\nИтого книг: {all_count}\n")

                if not flag:
                    print("\nНе найдено ни одной книги\n")
                    return 1

        except FileNotFoundError:
            print("\nПока что библиотека пуста, самое время пополнить ее\n")

    def delete(self):
        try:
            with open(self.data, encoding="utf-8") as file:
                data = json.load(file)
                if Library.read(self) == 1:
                    return 1
                remove_id = str(input("Напишите id удаляемой книги: "))
                flag = False
                for key, value in data.items():
                    if remove_id in value:
                        flag = True
                        removed = value.pop(remove_id)
                        print(
                            f"\nКнига успешно удалена:\n\n\t{key}: "
                            f"{removed[self.title]}({removed[self.year]}г.)\n"
                        )
                        break
                if not flag:
                    print("К сожалению данного id не существует")
                    if input("Попробовать еще раз (Enter/n): ") != "n":
                        Library.delete(self)
                    else:
                        return 0

            with open(self.data, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=2)

            if input('"y" - удалить еще, для выхода нажмите enter: ') == "y":
                Library().delete()
        except FileNotFoundError:
            print("\nК сожалению библиотека пуста, поэтому удалять нечего\n")

    def change_status(self):
        try:
            with open(self.data, encoding="utf-8") as file:
                data = json.load(file)
                if Library.read(self) == 1:
                    return
                id = str(input("id книги: "))
                flag = False
                for key, value in data.items():
                    if id in value:
                        flag = True

                        print(f"\nТекущий статус: {value[id][self.status]}")
                        inp = input(
                            """
        0 - Выдана
        1 - В наличии 


Ваш выбор: """
                        )

                        while inp not in ("0", "1"):
                            print(
                                f"\nТекущий статус: {value[id][self.status]}"
                            )
                            inp = input(
                                """
        0 - Выдана
        1 - В наличии 


Ваш выбор: """
                            )

                        value[id][self.status] = ("Выдана", "В наличии")[
                            int(inp)
                        ]
                        print(
                            f'\nТекущий статус у {key} "{value[id][self.title]}" - '
                            f"{value[id][self.status]}\n"
                        )
                if not flag:
                    print("К сожалению данного id не существует")
                    if input("Попробовать еще раз (Enter/n): ") != "n":
                        Library.change_status(self)

            with open(self.data, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=2)
        except FileNotFoundError:
            print(
                "\nОперация невозможна в связи с тем, что нет никаких данных\n"
            )
