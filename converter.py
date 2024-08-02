from openpyxl import load_workbook
import os
import csv


summa = 1
name_csv = 1

def fix_nulls(s):
    for line in s:
        yield line.replace('\0', '')

def create_file_csv(name_csv):
    if os.path.exists(f"{name_csv}.csv"):
        print("файл csv уже есть")
    else:
        with open(f"{name_csv}.csv", "w", encoding="utf-8") as file_data:
            writer = csv.writer(file_data)

            writer.writerow(
                (
                    'Поставщик',
                    'Артикул',
                    'Ценообразование',
                    'Закупка',
                    'Марка',
                    'Модель',
                    'Год',
                    'Объем двигателя',
                    'Топливо',
                    'Наименование запчасти',
                    'Номера деталей',
                    'Описание',
                    'Фото',
                    'Состояние',
                    'Скидка',
                    'Валюта',
                    'Удаляем дубли'
                )
            )
create_file_csv(name_csv)
# Указываем путь к директории
directory = "files_csv"
"""spisok_providers = []
book2= load_workbook("provider.xlsx")
sheet2= book2["Лист1"]
for i in range(2, 2000):
    providers = str(sheet2["B"+ str(i)].value)
    spisok_providers.append(providers)"""
# Получаем список файлов
summa_file = 0
files = os.listdir(directory)
for namefile in files:
    summa_file += 1 
# Выводим список файлов
    print(namefile)
    control = 0
    if "-" in namefile:
        provider = ""
        print("KARO")
        text = namefile[namefile.find("by-") +3 : namefile.find(".csv")]
        print(text)
        book= load_workbook("Таблица поставщиков.xlsx")
        sheet = book["Лист1"]
        
        for i in range(2, 2000):
            
            PB_provider = str(sheet["E"+ str(i)].value)
            if text in PB_provider:
                provider = str(sheet["B"+ str(i)].value)
                pricing = str(sheet["C"+ str(i)].value)
                control = 1

        if control != 1:
            if "PB" not in provider:
                pricing = 3
                provider = "PB_&&&"
        
        print(pricing, provider)
        with open(f'files_csv/{namefile}', 'r', encoding="utf-8") as csvfile:
            csvreader = csv.reader(fix_nulls(csvfile))
            n = 1
            p = 1
            
            for row in csvreader:
                
                if p > 1:
                    if summa < 500000 :

                        #print(row)
                        row = str(row)
                        stroka = row.split(";")
                        #for symbol in stroka:
                        #    print(symbol)
                        marka = stroka[1].replace('"',"").replace("'","")
                        model = stroka[2].replace('"',"").replace("'","")
                        year = stroka[3].replace('"',"").replace("'","")
                        volume = stroka[6].replace('"',"").replace("'","")
                        fuel = stroka[5].replace('"',"").replace("'","")
                        name_part = stroka[4].replace('"',"").replace("'","")
                        num_zap = stroka[10].replace('"',"").replace("'","")
                        info = stroka[11].replace('"',"").replace("'","")
                        price = stroka[12].replace('"',"").replace("'","")
                        val = stroka[13].replace('"',"").replace("'","")
                        artical = stroka[0].replace('"',"").replace("['","").replace("'","")
                        foto = stroka[17].replace('"',"").replace("'","")
                        sale = stroka[14].replace('"',"").replace("'","")
                        status = stroka[19].replace('"',"").replace("'","")
                        if status == "1":
                            status = "Новая"
                        else:
                            status = "б/у"

                        file = open(f"{name_csv}.csv", "a", encoding="utf-8", newline='')
                        writer = csv.writer(file)

                        writer.writerow(
                            (
                                provider,
                                artical,
                                pricing,
                                price,
                                marka,
                                model,
                                year,
                                volume,
                                fuel,
                                name_part,
                                num_zap,
                                info,
                                foto,
                                status,
                                sale,
                                val,
                                'Удаляем дубли'
                            )
                        )
                        file.close()
                        summa += 1
                    else:
                        summa = 1
                        name_csv += 1
                        create_file_csv(name_csv)

                else:
                    p += 1

    else:
        provider = ""
        print("driver")
        text = namefile[: namefile.find(".csv")]
        print(text)
        book= load_workbook("Таблица поставщиков.xlsx")
        sheet = book["Лист1"]
        
        for i in range(2, 2000):
            
            PB_provider = str(sheet["D"+ str(i)].value)
            if text == PB_provider:
                provider = str(sheet["B"+ str(i)].value)
                pricing = str(sheet["C"+ str(i)].value)
                control = 1

        if control != 1:
            if "PB" not in provider:
                pricing = 3
                provider = "PB_&&&"

            
        print(pricing, provider)
        with open(f'files_csv/{namefile}', 'r', encoding="utf-8") as csvfile:
            csvreader = csv.reader(fix_nulls(csvfile))
            n = 1
            p = 1
            for row in csvreader:
                if p > 1:
                    if summa < 500000 :    
                        #print(row)
                        row = str(row)
                        stroka = row.split(";")
                        #for symbol in stroka:
                        #     print(symbol)
                        
                        marka = stroka[0].replace("['","").replace('"""',"")
                        model = stroka[1].replace('"""',"")
                        year = stroka[2].replace('"""',"")
                        volume = stroka[3].replace('"""',"")
                        fuel = stroka[4].replace('"""',"")
                        name_part = stroka[8].replace('"""',"")
                        num_zap = stroka[9].replace('"""',"")
                        info = stroka[10].replace('"""',"").replace("'","")
                        price = stroka[11].replace('"""',"")
                        val = stroka[12].replace('"""',"")
                        artical = stroka[13].replace('"""',"")
                        foto = stroka[14].replace('"""',"").replace("'","")
                        sale = stroka[15].replace('"""',"")
                        status = stroka[16].replace('"""',"")
                        if status == "1":
                            status = "Новая"
                        else:
                            status = "б/у"
                        #print(provider)
                        #print(marka, model, year, volume, fuel, name_part, num_zap, info, price, val, artical, foto, sale, status, pricing, provider)
                        
                        file = open(f"{name_csv}.csv", "a", encoding="utf-8", newline='')
                        writer = csv.writer(file)

                        writer.writerow(
                            (
                                provider,
                                artical,
                                pricing,
                                price,
                                marka,
                                model,
                                year,
                                volume,
                                fuel,
                                name_part,
                                num_zap,
                                info,
                                foto,
                                status,
                                sale,
                                val,
                                'Удаляем дубли'
                            )
                        )
                        file.close()
                        summa += 1
                    else:
                        summa = 1
                        name_csv += 1
                        create_file_csv(name_csv)
        
                    
                else:
                    p += 1

print("Всего обработано {summa_file} файлов")

input("Нажми любую кнопку, чтобы закончить")
    
        