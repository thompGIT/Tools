#!/usr/bin/python

import urllib2;
import re;

# ls1gto.com 'For Sale' forum
page = 'http://www.ls1gto.com/forums/forumdisplay.php?f=19';
token_begin = '<!-- show threads -->';
token_end   = '<!-- end show threads -->';

def processPost(html):
    results = []
    titles = re.findall('e_[0-9]*">.*<', html);
    times  = re.findall('[0-9].*time.*M', html);
    descriptions = re.findall('', html);
    for title, time in zip(titles,times):
        title = title[title.find('>')+1:-1];
        time  = time[time.find('>')+1:] + ' ' + time[:time.find('<')-1];
        results.append((title,time));
    return results;

# Grab the web content
print ('Scanning page: ' + page);
html = urllib2.urlopen(page).read();

# Discard the useless parts
begin = html.find(token_begin);
end   = html.find(token_end, begin);
result = html[begin:end]

# Process each post
results = processPost(result);

for x in results:
    print (x);
