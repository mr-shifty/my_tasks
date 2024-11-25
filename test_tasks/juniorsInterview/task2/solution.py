import csv

import requests
from bs4 import BeautifulSoup

russianAlphabet: str = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

animalCounts: dict = {letter: 0 for letter in russianAlphabet}

url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

for link in soup.select(".mw-category-group"):
    letter = link.find("h3").get_text(strip=True)[0]

    if letter in animalCounts:
        animals = link.select("ul li a")

        animalCounts[letter] += len(animals)

with open("beasts.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for letter, count in animalCounts.items():
        writer.writerow([letter, count])

print("Данные успешно записаны в beasts.csv")
