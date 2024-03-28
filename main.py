import csv
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

with open("BMW PARTS_2_SD_147949.csv", "r") as f:
    reader = csv.reader(f, delimiter=';')

    with open("new.csv", "w") as f:
        header = [
            "МАРКА",
            "МОДЕЛЬ",
            "ГОД",
            "ОБЪЕМ ДВИГАТЕЛЯ",
            "ТОПЛИВО",
            "ТИП ДВИГАТЕЛЯ",
            "КОРОБКА",
            "ТИП КУЗОВА",
            "НАИМЕНОВАНИЕ ЗАПЧАСТИ",
            "НОМЕР ДЕТАЛИ",
            "НОМЕРА ЗАМЕН",
            "ОПИСАНИЕ",
            "ЦЕНА",
            "ВАЛЮТА",
            "ID_EXT",
            "ФОТО",
            "СКИДКА",
            "НОВАЯ ДЕТАЛЬ",
        
        ]
        writer = csv.DictWriter(f, fieldnames=header)

        writer.writeheader()
        for line in reader:
            print(line)
