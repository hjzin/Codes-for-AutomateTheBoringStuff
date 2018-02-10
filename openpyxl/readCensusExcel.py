#! /usr/bin/env/python3
#-*- coding: utf-8-*-
#计算每个地区的人口数及人口普查区的个数

import openpyxl,pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.active
countyData = {}

print('Reading rows..')
for row in range(2, sheet.max_row +1):
	state = sheet['B' + str(row)].value
	county = sheet['C'+ str(row)].value
	pop = sheet['D'+ str(row)].value
	
	countyData.setdefault(state,{})
	countyData[state].setdefault(county, {'tracts':0, 'pop': 0})
	countyData[state][county]['tracts'] += 1
	countyData[state][county]['pop'] += int(pop)

#write result to a file
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = '+ pprint.pformat(countyData))
resultFile.close()
print('Done')

