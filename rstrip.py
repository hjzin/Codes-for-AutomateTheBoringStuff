#!/usr/bin/env/python3
#-*- coding:utf-8 -*-

#用正则表达式实现类似strip()方法的功能，可以去掉一个字符串首尾的指定字符，默认为空格。

import re
def rstrip(text, char=' '):
	'''

	匹配字符串中首尾的指定字符并将其去掉，如果没有找到指定的字符则返回原字符串

	text:原字符串
	char:要去掉的字符串，默认为空格

	'''
	string=re.compile(r'^(%s)*|(%s)*$'%(char,char))
	print(string.sub('',text))

text='    sfdlfjsl   sdfsdfjls '
rstrip(text,'s')
