#! /usr/bin/env/python3
#-*- coding:utf-8 -*-
#更改表格中指定产品的价格

import openpyxl

# open the file
wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.active
# 待更新的值
price_update = {
	'Celery': 1.18,
	'Garlic': 3.06,
	'Lemon': 1.25,
}

print('Searching...')

for rowNum in range(2, sheet.max_row):
	produceName = sheet.cell(row = rowNum, column = 1).value
	if produceName in price_update:
		sheet['B' + str(rowNum)].value = price_update[produceName]

print('Done')
wb.save('produceSales.xlsx')
