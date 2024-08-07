import json
import time
from typing import Any, Dict, Union

from validator import check_year, find_match


class Library:
    def __init__(self) -> None:
        """
        Инициализация объекта библиотеки с начальными значениями.
        """
        self.id = int(time.time() * 1000)
        self.data = "data.json"
        self.title = "Название книги"
        self.author = "Автор"
        self.year = "Год издания"
        self.status = "Статус книги"

    def search(self) -> int:
        """
        Поиск книг в библиотеке по названию, автору или году издания.
        Возвращает 1, если ничего не найдено, и 0 в случае успеха.
        """
        try:
            with open(self.data, encoding="utf-8") as file:
                data: Dict[str, Dict[str, Dict[str, Any]]] = json.load(file)
                search_data = input(
                    "\nВведите название, автора или год издания книги: "
                ).lower()
                flag = False
                for key, value in data.items():
                    if value:
                        if find_match(key, search_data):
                            flag = True
                            print(f"\nАвтор: {key}\nКниги:")
                            for k, v in value.items():
                                print(
                                    f"\tid: {k}\n"
                                    f"\tНазвание: {v[self.title]}\n"
                                    f"\tГод издания: {v[self.year]}\n"
                                    f"\tСтатус: {v[self.status]}\n"
                                )
                        else:
                            for k, v in value.items():
                                if find_match(
                                    search_data, v[self.title]
                                ) or find_match(search_data, v[self.year]):
                                    flag = True
                                    print(f"\nАвтор: {key}\nКниги:")
                                    print(
                                        f"\tid: {k}\n"
                                        f"\tНазвание: {v[self.title]}\n"
                                        f"\tГод издания: {v[self.year]}\n"
                                        f"\tСтатус: {v[self.status]}\n"
                                    )

            if not flag:
                print("\nК сожалению ничего не найдено\n")
                return 1
            return 0

        except FileNotFoundError:
            print(
                "\nНичего не найдено в пустоте, самое время добавить первую книгу\n"
            )
            return 1

    def create(self) -> None:
        """
        Создание нового файла библиотеки и добавление первой книги.
        """
        with open(self.data, "w", encoding="utf-8", errors="ignore") as file:
            dct = {
                input("Введите автора: "): {
                    self.id: {
                        self.title: input("Введите название книги: "),
                        self.year: check_year(input("Введите год: ")),
                        self.status: "В наличии",
                    },
                },
            }
            json.dump(dct, file, indent=2)
        print("\nКнига успешно добавлена\n")

    def update(self) -> None:
        """
        Обновление существующего файла библиотеки путем добавления новой книги.
        """
        with open(self.data, encoding="utf-8", errors="ignore") as file:
            self.id = int(time.time() * 1000)
            data: Dict[str, Dict[str, Dict[str, Any]]] = json.load(file)
            self.author = input("Введите автора: ")
            if self.author not in data:
                data.update(
                    {
                        self.author: {
                            self.id: {
                                self.title: input("Введите название книги: "),
                                self.year: check_year(input("Введите год: ")),
                                self.status: "В наличии",
                            },
                        },
                    },
                )
            else:
                data[self.author][self.id] = {
                    self.title: input("Введите название книги: "),
                    self.year: check_year(input("Введите год: ")),
                    self.status: "В наличии",
                }
        print("\nКнига успешно добавлена\n")

        with open(self.data, "w", encoding="utf-8", errors="ignore") as file:
            json.dump(data, file, indent=2)

    def read(self) -> Union[int, None]:
        """
        Чтение и отображение всех книг в библиотеке.
        Возвращает 1, если не найдено ни одной книги.
        """
        try:
            with open(self.data, encoding="utf=8") as file:
                data: Dict[str, Dict[str, Dict[str, Any]]] = json.load(file)
                flag = False
                all_count = 0
                for key, value in data.items():
                    if value:
                        flag = True
                        print(
                            f"\nАвтор: {key} ({len(value.values())} шт.)\nКниги:"
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

    def delete(self) -> Union[int, None]:
        """
        Удаление книги из библиотеки по ID.
        Возвращает 1, если ID не существует.
        """
        try:
            with open(self.data, encoding="utf-8") as file:
                data: Dict[str, Dict[str, Dict[str, Any]]] = json.load(file)
                remove_id = str(input("\nНапишите id удаляемой книги: "))
                flag = False
                for key, value in data.items():
                    if remove_id in value:
                        flag = True
                        inp = input(
                            f"\nНайдена {key}: {''.join(map(lambda x: x[self.title], value.values()))}."
                            " Удаляем? (y/n) "
                        )
                        match inp:
                            case "y":
                                removed = value.pop(remove_id)
                                print(
                                    f"\nКнига успешно удалена:\n\n\t{key}: {removed[self.title]} ({removed[self.year]}г.)\n"
                                )
                                break
                            case "n":
                                print("\nОперация отменена\n")
                                return
                            case _:
                                print("Неверный ответ, операция не выполнена")
                                return
                if not flag:
                    print("К сожалению данного id не существует")
                    return 1

            with open(self.data, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=2)
            return 0

        except FileNotFoundError:
            print("\nК сожалению библиотека пуста, поэтому удалять нечего\n")

    def change_status(self) -> None:
        """
        Изменение статуса книги в библиотеке по ID.
        """
        try:
            with open(self.data, encoding="utf-8") as file:
                data: Dict[str, Dict[str, Dict[str, Any]]] = json.load(file)
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
                            f'\nТекущий статус у {key} "{value[id][self.title]}" - {value[id][self.status]}\n'
                        )
                if not flag:
                    print("К сожалению данного id не существует")
                    if input("Попробовать еще раз (Enter/n): ") != "n":
                        self.change_status()

            with open(self.data, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=2)
        except FileNotFoundError:
            print(
                "\nОперация невозможна в связи с тем, что нет никаких данных\n"
            )
