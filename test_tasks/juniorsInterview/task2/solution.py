import csv

import requests
from bs4 import BeautifulSoup

russian_alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

animal_counts = {letter: 0 for letter in russian_alphabet}

url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

for link in soup.select(".mw-category-group"):
    letter = link.find("h3").get_text(strip=True)[0]

    if letter in animal_counts:
        animals = link.select("ul li a")

        animal_counts[letter] += len(animals)

with open("beasts.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for letter, count in animal_counts.items():
        writer.writerow([letter, count])

print("Данные успешно записаны в beasts.csv")
