#! /usr/bin/env/python3
#-*- coding:utf-8 -*-
#下载xkcd漫画

import requests, os, bs4
url = 'http://xkcd.com'		#网页的url
os.makedirs('./xkcd',exist_ok = True)	#将下载的内容存在文件夹中

while url != 'http://xkcd.com/1945/':
	#下载网页
	print('Downloading page %s' %url)
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text, "html.parser")

	#得到漫画图片的URL
	comicElem = soup.select('#comic img')
	if comicElem == []:
		print('Could not find comic image.')
	else:
		comicUrl = 'https:' + comicElem[0].get('src')
		#下载漫画图片
		res = requests.get(comicUrl)
		res.raise_for_status()

	#将文件存到相应文件夹中
	imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
	for chunk in res.iter_content(100000):
		imageFile.write(chunk)
	imageFile.close()

	#得到之前漫画的URL
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prevLink.get('href')

print('Done')