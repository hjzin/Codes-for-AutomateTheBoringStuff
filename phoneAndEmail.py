#!/usr/bin/env/python3
#-*- coding: utf-8 -*-
#在文本中查找电话号码和电子邮箱地址并复制到剪贴板上

import pyperclip, re

#匹配电话号码
phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?				#area code(optional)
	(\s|-|\.)						#separator
	(\d{3})							#first 3 digits
	(\s|-|\.)						#separator
	(\d{4})							#first 4 digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?	#extension(optional)
	)''', re.VERBOSE)

#匹配电子邮件地址
emailRegex = re.compile(r'''(
	[a-zA-z0-9._%+-]+				#username
	@								#@
	[a-zA-z0-9.-]+					#domain name
	(\.[a-zA-z]{2,4})				#dot-something
	)''', re.VERBOSE)

#匹配文本内容
text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)

for groups in emailRegex.findall(text):
	matches.append(groups[0])

#将匹配内容复制到剪切板
if len(matches) >0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard')
	print('\n'.join(matches))
else:
	print('No phone numbers or email address found.')

