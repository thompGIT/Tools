#!/usr/bin/python

import zipfile
import re

# Build the dictionary
def buildDictionary(infile):
	f = open(infile)
	d = f.read().splitlines()
	f.close()
	return d

# Unzip a file to a folder
def unzip(infile, dest):
	zip = zipfile.ZipFile(infile,'r')
	zip.extractall(dest)

# Injest the document
def readDoc(infile):
	f = open(infile)
	text = ''
	for line in f:
		text += line
	f.close()
	return text

dictionary = buildDictionary('dictionary')
unzip('Test.docx','temp')
words = readDoc('temp/word/document.xml')
words = re.sub(r"<[^>]*.", "", words)
print words
