from openpyxl import load_workbook

book = load_workbook("first.xlsx")

for item in book:
    print(item)
    break