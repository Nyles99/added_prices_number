import json
import time
import requests
from bs4 import BeautifulSoup
import os
import csv
from PIL import Image, ImageFile, UnidentifiedImageError
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

headers = {
    "Accept" : "application/json, text/javascript, */*; q=0.01",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

url = "https://bamper.by/personal/import/bamper_marki-modeli.php"

marka_model = {}

black_list = []
black_mark = []
black_model = []

file1 = open("black-list.txt", "r")
while True:
    # считываем строку
    line = file1.readline()
    line = line.replace("\n","").replace("'","").replace(" ","")
    # прерываем цикл, если строка пустая
    if not line:
        break
    # выводим строку
    black_list.append(line)
#print(black_list)
# закрываем файл
file1.close

file1 = open("black-mark.txt", "r", encoding="utf-8")
while True:
    # считываем строку
    line = file1.readline()
    line = line.replace("\n","").replace("'","").replace(" ","")
    # прерываем цикл, если строка пустая
    if not line:
        break
    # выводим строку
    black_mark.append(line)
#print(black_list)

# закрываем файл
file1.close

file1 = open("black-model.txt", "r", encoding="utf-8")
while True:
    # считываем строку
    line = file1.readline()
    line = line.replace("\n","").replace("'","").replace(" ","")
    # прерываем цикл, если строка пустая
    if not line:
        break
    # выводим строку
    black_model.append(line)
#print(black_list)




req = requests.get(url=url, headers=headers)
src = req.text
soup_1 = BeautifulSoup(src, 'html.parser')
href_part = soup_1.find("div", class_="content")
#print(href_part)
href_part = str(href_part).split("<h5>")
#print(href_part)
for stroka in href_part:
    #print(stroka,"новая строка")
    marka = stroka[: stroka.find("</h5>")]
    print(marka)
    if marka not in black_mark:
        stroka_1 = str(stroka).split("<br/>")
        #print(stroka_1)
        for mod in stroka_1:
            model = mod[mod.find("amp;nbsp")+ 8 :]
            print(model)
            if model not in black_model:
                if marka != " " and model != " ":
                    marka_model[model] = marka  
with open("marka_model.json", "a", encoding="utf-8") as file:
    json.dump(marka_model, file, indent=4, ensure_ascii=False) 
"""for item in href_part:
    item = str(item)
    print(item)
    mark = item[item.find("<h5>")+ 4 : item.find("</h5>")]
    print(mark, "Тут пробел")"""