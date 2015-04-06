#!/usr/bin/python

import sqlite3 as sql;
import sys
import urllib2;
import re;
from collections import namedtuple
import datetime
import smtplib
from email.mime.text import MIMEText

# Relative path to the database
DB_PATH = 'scout.db'

#TODO: Get named tuples working 
# Structures
Search = namedtuple("Search", "site_url trim_begin trim_end re_title re_date re_description description")

# Send an email to announce a new interesting post
def emailAnnounce(msg_text):
    msg = MIMEText(msg_text)
    msg['Subject'] = 'New Post!'
    msg['From'] = 'scout'
    msg['To']   = 'jamesdavidthompson@gmail.com'
    s = smtplib.SMTP('smtp-server.cfl.rr.com')
    s.sendmail('thomp@cfl.rr.com', 'jamesdavidthompson@gmail.com', msg.as_string())
    s.quit()

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
    print '       terms:', 
    tString = ''
    for t in terms:
        tString += t + ', '
    tString = tString[:-2]
    print tString
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

    print 'Stats:\n\ttitles: %s\n\t dates: %s\n\t  desc: %s\n\t   ids: %s' % (len(titles), len(dates), len(descriptions), len(ids))

    # TODO: Remove the trims specific to ls1gto.com
    # 
    posts = []
    # for t, dt, d, i in zip(titles,dates,descriptions,ids):
    for t, dt, i in zip(titles,dates,ids):
        title = t[t.find('>')+1:-1]
        date  = datetime.datetime.now()
        # desc  = d[d.find('="')+2:-2]
        desc  = ''
        pid   = i[i.find('_')+1:-2]
        posts.append((pid,title,date,desc))

    # Register interesting posts
    newPosts = []
    for p in posts:
        if ( registerPost(p) == 0 ):
            # print 'New Post: %s' % p[1]
            newPosts.append(p)

    # Check new posts for interest
    interestingPosts = []
    for p in newPosts:
        for t in terms:
            if (p[1].find(t) >= 0):
                print 'New Interesting Post: %s' % p[1]
                interestingPosts.append(p)
                break

    # Announce new interesting posts
    for p in interestingPosts:
        url = 'http://www.ls1gto.com/forums/showthread.php?t=%s' % p[0]
        emailAnnounce('Subject: %s\nUrl: %s\nTerms: %s' % (p[1],url,tString))

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
        # print "Error %s:" % e.args[0]
        return 1
    finally:
        if con:
            con.close()
    return 0

# Main
searches = getSearches()
search_terms = getSearchTerms()
for s in searches:
    processSearch(s,search_terms)
