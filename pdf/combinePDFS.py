#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
#合并多个pdf

import os
import PyPDF2

#get the PDF filenames
pdfFiles = []
for filename in os.listdir('.'):
	if filename.endswith('pdf'):
		pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

#open each file
for filename in pdfFiles:
	pdfFileObj = open(filename, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	#loop through pages
	for pagenum in range(1, pdfReader.numPages):
		pageObj = pdfReader.getPage(pagenum)
		pdfWriter.addPage(pageObj)

#save the result file
pdfOutPut = open('combinedPdf.pdf', 'wb')
pdfWriter.write(pdfOutPut)
pdfOutPut.close()
