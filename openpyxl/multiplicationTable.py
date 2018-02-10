#! /usr/bin/env/python3
#-*- coding: utf-8 -*-
#自动生成N*N的乘法表

import openpyxl
import sys
#open file
wb = openpyxl.Workbook()
sheet = wb.active

#writing file
print('writing...')

if len(sys.argv) == 2:
	num = int(sys.argv[1])
	#初始化
	for i in range(1,num+1):
		sheet['A' + str(i+1)] = i
		sheet.cell(row = 1,column = i+1).value = i
	#向表格中写入数字
	for j in range(2,num+2):
		for k in range(2,num+2):
			sheet.cell(row = j, column = k).value = sheet['A' + str(j)].value * sheet.cell(row = 1, column = k).value

	wb.save('multiplicationTable.xlsx')
	print('Done')
else:
	print('required 2 arguments!')
