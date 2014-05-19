#!/usr/bin/python

#===========================================================
# wordhistogram.py
#
# Creates a histogram based of a MS Word .docx based on a 
#  predefined dictionary.
#===========================================================

import sys
import shutil
import zipfile
import re
import operator

def printUsage():
	print 'Usage:\n wordhistogram infile dictionary'
	print ''
   
def createReport(results, outfile):	
	reportXML  = '<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="report.xsl"?>\n'
	reportXML += '<report>\n'
	for item in results:
		reportXML += '<entry>\n<word>%s</word>\n<count>%s</count>\n</entry>\n' % (item[0], item[1])
	reportXML += '</report>\n'
	f = open(outfile, 'w')
	f.write(reportXML)
	f.close()

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
def readDocx(infile):
	unzip(infile,'temp')
	f = open('temp/word/document.xml')
	text = ''
	for line in f:
		text += line.lower()
	f.close()
	shutil.rmtree('temp')
	text = re.sub(r"<[^>]*.", "", text)
	return text

# Create a global histogram
def createHistogram(string):
	results = {}
	words = re.findall('[\w]+',string)
	for word in words:
		word = word.lower()
		if word not in results:
			results[word] = 0
		results[word] += 1
	results = sorted(results.iteritems(), key=operator.itemgetter(1), reverse=True)
	return results

# Create the histogram
def createDictionaryHistogram(dictionary, string):
	results = {} 
	for entry in dictionary:
		regex = entry.lower()
		count = len(re.findall(regex, string))
		results[entry] = count
	results = sorted(results.iteritems(), key=operator.itemgetter(1), reverse=True)
	return results

# Format and print the results
def printResults(output):
	print ' %15s %3s' % ('Dictionary  ','Cnt')
	print ' %15s %3s' % ('===============','===')
	for item in output:
		print ' %15s %3s' % (item[0], item[1])

# Process command line args
if (len(sys.argv) != 3): 
	printUsage()
	exit(1)

# Extract text from the input file
words = readDocx(sys.argv[1])

# Build the dictionary
dictionary = buildDictionary(sys.argv[2])

# Create the raw histogram
hist = createHistogram(words)

# Create the dictionary histogram
results = createDictionaryHistogram(dictionary,words)

# Print the output
#print '---------------------'
#print 'Dictionary Hits'
#printResults(results)
createReport(results,sys.argv[1] + '.DictHits.xml')
#print '---------------------'

# Print the output
#print '\n'
#print '---------------------'
#print 'Document Histogram'
#printResults(hist)
createReport(hist,sys.argv[1] + '.Hist.xml')
#print '---------------------'
