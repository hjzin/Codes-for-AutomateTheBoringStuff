#! /usr/bin/env/python3
#-*- coding:utf-8 -*-
#可以复制多个字符串的剪贴板

#Usage: python3 multiclipboard.pyw save <keyword> - Save clipboard to keyword
#		python3 multiclipboard.pyw <keyword> - loads keyword to clipboard
#		python3 multiclipboard.pyw list - load all keywords to clipboard
#		python3 multiclipboard.pyw delete <keyword> - Delete the keyword

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
# Save clipboard content
if len(sys.argv) == 3 :
	if sys.argv[1].lower() == 'save':
		mcbShelf[sys.argv[2]]= pyperclip.paste()
	elif sys.argv[1].lower() == 'delete':
		del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
	#List keyword and load content.
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()

