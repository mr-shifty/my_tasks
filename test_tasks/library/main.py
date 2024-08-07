import os

from handler import Library

library = Library()


def main():
    """
    Отображает главное меню и обрабатывает ввод пользователя для системы библиотеки.
    Пользователь может добавлять, удалять, находить, отображать или изменять статус книг.
    """

    print(
        """
          ______________________________
         |                              |
         |          MY LIBRARY          | 
         |                              |
         |   1. Добавить книгу          |
         |   2. Удалить книгу           |
         |   3. Найти книгу             |
         |   4. Отобразить все книги    |
         |   5. Изменить статус книги   |
         |                              |
         |          Выход(q)            |
         |          --------            |
         |______________________________|
         """
    )
    match input("Введите число для выбора (1-5) или q для выхода: "):
        case "1":
            (
                library.update()
                if os.path.exists("data.json")
                else library.create()
            )
            inp = input('"y" - добавить еще, для выхода нажмите enter: ')
            while inp == "y":
                library.update()
                inp = input('"y" - добавить еще, для выхода нажмите enter: ')

        case "2":
            while True:
                delete = library.delete()
                match delete:
                    case 0:
                        if (
                            input(
                                '"y" - удалить еще, для выхода нажмите enter: '
                            )
                            != "y"
                        ):
                            break
                    case 1:
                        if input("Попробовать еще раз (Enter/n): ") == "n":
                            break
                    case _:
                        break
        case "3":
            library.search()
        case "4":
            library.read()
        case "5":
            library.change_status()
        case "q":
            exit()
        case _:
            print("Введите число от 1 до 5 или q для выхода: ")
            main()
    main()


if __name__ == "__main__":
    main()
