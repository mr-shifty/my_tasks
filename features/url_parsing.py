import pretty_errors
from math import factorial


with open("url.txt", "w", encoding="utf-8") as url:
    text = input()
    url.write(f"Текст:\n\n{text}\n\nДетали:\n")

    pattern = r"(?P<Протокол>https?)://(?P<Домен>[a-z\.]+)/(?:[\/\-\w]+)?(?P<Параметры>\?[a-z=&0-9]+)?(?P<Якорь>#[a-z]+)?"

    result = __import__("re").finditer(pattern, text)

    for item in result:
        url.write(
            f"""\nПолная ссылка: {item.group()}
Протокол: {item.group("Протокол")} | Домен: {item.group("Домен")} | Параметры: {item.group("Параметры")} | Якорь: {item.group('Якорь')}\n"""
        )
