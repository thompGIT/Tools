#!/usr/bin/python

import sqlite3 as sql;
import sys
import urllib2;
import re;
from collections import namedtuple

# Relative path to the database
DB_PATH = 'scout.db'

#TODO: Get named tuples working 
# Structures
Search = namedtuple("Search", "site_url trim_begin trim_end re_title re_date re_description description")


# Process a search
def processSearch(search,terms):

    url        = search[0]
    trim_begin = search[1]
    trim_end   = search[2]
    re_title   = search[3]
    re_date    = search[4]
    re_id      = search[5]
    re_desc    = search[6]

    print '[Search Details]'
    print '         url: %s' % url
    print '  trim_begin: %s' % trim_begin
    print '    trim_end: %s' % trim_end
    print '    re_title: %s' % re_title
    print '     re_date: %s' % re_date
    print '       re_id: %s' % re_id
    print '     re_desc: %s' % re_desc
    print ''

    # Grab the web content
    print ('Scanning page: ' + url)
    html = urllib2.urlopen(url).read()

    # Discard the useless parts
    begin = html.find(trim_begin)
    end   = html.find(trim_end, begin)
    html = html[begin:end]

    # Extract the goodies
    titles       = re.findall(re_title, html)
    dates        = re.findall(re_date,  html)
    descriptions = re.findall(re_desc,  html)
    ids          = re.findall(re_id,    html)

    # TODO: Remove the trims specific to ls1gto.com
    # 
    posts = []
    for t, dt, d, i in zip(titles,dates,descriptions,ids):
        title = t[t.find('>')+1:-1];
        date  = dt;
        desc  = d[d.find('="')+2:-2];
        pid   = i[i.find('_')+1:-2];
        posts.append((pid,title,date,desc))

    # Register interesting posts
    for p in posts:
        registerPost(p)

#TODO: Create a common db search function to clean this up
# Return list of searches
def getSearches():
    QUERY = "SELECT site_url, trim_begin, trim_end, re_title, re_date, re_id, re_description FROM searches"
    try:
        con = sql.connect(DB_PATH)
        cur = con.cursor()
        cur.execute(QUERY)
        results = []
        for row in cur.fetchall():
            results.append((row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
    except sql.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
    finally:
        if con:
            con.close()
    return results

# Return list of search terms
def getSearchTerms():
    QUERY = "SELECT term FROM search_terms"
    try:
        con = sql.connect(DB_PATH)
        cur = con.cursor()
        cur.execute(QUERY)
        results = []
        for row in cur.fetchall():
            results.append(row[0])
    except sql.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
    finally:
        if con:
            con.close()
    return results

# Add an entry to the database
def registerPost(post):
    pid   = post[0]
    title = post[1]
    date  = post[2]
    desc  = post[3]
    try:
        con = sql.connect(DB_PATH)
        cur = con.cursor()
        cur.execute('INSERT INTO posts (id,title,date,description) VALUES (?,?,?,?)', (pid,title,date,desc))
        con.commit()
    except sql.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
    finally:
        if con:
            con.close()

# Main
searches = getSearches()
search_terms = getSearchTerms()
for s in searches:
    processSearch(s,search_terms)
