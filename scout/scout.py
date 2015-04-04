#!/usr/bin/python

import sqlite3 as sql;
import sys
import urllib2;
import re;
from collections import namedtuple

# Relative path to the database
DB_PATH = 'scout.db'

# Structures
Search = namedtuple("Search", "site_url trim_begin trim_end re_title re_data re_description description")

def processSearch(html):
    results = []
    titles = re.findall('e_[0-9]*">.*<', html);
    times  = re.findall('[0-9].*time.*M', html);
    descriptions = re.findall('', html);
    for title, time in zip(titles,times):
        title = title[title.find('>')+1:-1];
        time  = time[time.find('>')+1:] + ' ' + time[:time.find('<')-1];
        results.append((title,time));
    return results;


# Return list of searches
def getSearches():
    QUERY = "SELECT site_url, trim_begin, trim_end, re_title, re_date, description FROM searches"
    try:
        con = sql.connect(DB_PATH)
        cur = con.cursor()
        cur.execute(QUERY)
        results = []
        for row in cur.fetchall():
            results.append((row[0],row[1],row[2],row[3],row[4],row[5]))
    except sql.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
    finally:
        if con:
            con.close()
    return results

# Main
searches = getSearches()
print searches





'''
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
'''
