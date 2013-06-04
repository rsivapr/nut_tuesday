#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib2
import time

hdr = { 'User-Agent' : 'trying to consoliate Nutrition Tuesday for fitness wiki by /u/bloometal/' }


redditFile = urllib2.urlopen("http://www.reddit.com/r/Fitness/comments/1ermqp/nutrition_tuesday/")
redditHtml = redditFile.read()
redditFile.close()

soup = BeautifulSoup(redditHtml)
print soup.find("blockquote").p.string



thang=soup.find_all('div',{'class':'md'})
next = thang[1].p.a.get('href')
"""
redditFile = urllib2.urlopen("http://www.reddit.com/r/Fitness/comments/1ermqp/nutrition_tuesday/")
redditHtml = redditFile.read()
redditFile.close()
"""
for i in range(15):
    time.sleep(10)
    soup = BeautifulSoup(urllib2.urlopen(next))
    print i, soup.find("blockquote").p.string
    thang=soup.find_all('div',{'class':'md'})
    next = thang[1].p.a.get('href')

#for each in thang:
#print each
#print each['href']+","+each.string
#redditAll = soup.find_all("a")
    #for links in soup.find_all("blockquote"):
    #for links in soup.findAll("a", attrs={'class': None}):
#print links
    #print (links.get('href'))
