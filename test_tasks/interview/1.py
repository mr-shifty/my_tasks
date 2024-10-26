"""
Cоздает список, который выглядит как lst = [[], [], []]. 
Однако, все три элемента списка ссылаются на один и тот же объект (пустой список). 
Это означает, что изменения в одном из этих списков отразятся на всех.

"""

# lst = [[]] * 3
#
# lst[1].append(1)
# print(lst)

"""
В Python оператор is используется для проверки, 
ссылаются ли две переменные на один и тот же объект в памяти.
В Python небольшие целые числа (обычно от -5 до 256) кэшируются,
и для них используется один и тот же объект.
"""

# big_num_1 = 1000
# big_num_2 = 1000
# small_num_1 = 1
# small_num_2 = 1
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(big_num_1 is big_num_2) #False, тк числа больше 256 и не кешируется
# print(small_num_1 is small_num_2) #True
# print(lst1 is lst2)

"""
Сделать копию словаря или преобразовать в список,
тк удаление во время итерации приводит к ошибке
"""
# numbers = {1: "один", 2: "два", 3: "три"}
# for number in numbers:  # Сделать копию или преобразовать в список,
#     if numbers[number] == "два":
#         del numbers[number]
# print(numbers)

"""
В Python при использовании срезов (slice) на списках не возникает ошибки,
даже если указанный индекс выходит за пределы длины списка. 

Когда вы делаете срез, Python просто возвращает пустой список,
если начальный индекс больше, чем длина списка
"""
# lst = ["a", "b", "c", "d", "e"]
# print(lst[10:])

"""
Декоратор
"""
# def print_hello():
#     def wrapper(func):
#         print("Hello world!!!")
#         return func
#
#     return wrapper
#
#
# @print_hello()
# def print_hi():
#     print("Привет")
#
#
# print_hi()


class Person:
    """
    Ответ 123 ЕЁЖЗ, тк присваиваемое новое значение "ГДЕ"
    не влияет на уже созданный объект person.
    """

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


first_name = "123"
person = Person(first_name, "АБВ")
first_name = "ГДЕ"
person.last_name = "ЕЁЖЗ"
# print(person.first_name, person.last_name)


"""
• @classmethod: Метод класса с доступом к классу.

• @staticmethod: Статический метод без доступа к классу или экземпляру.

• @property: Свойство для управления доступом к атрибутам класса.
"""
# @classmethod, @staticmethod, @property
