#!/usr/bin/python

from urllib.request import Request, urlopen
import musicbrainzngs
import random
import json 
import ast
import statistics 

# Variables
songslist = []
countlist = []
songNumber=[]
n = 0
xx = 0
r=random.sample(range(16), 5)

for i in range(5):
    songNumber.append(r[xx])
    xx += 1

# setting user agent
musicbrainzngs.set_useragent("LyricsWordCount", "1.0", "azizn03",) 

# User input
artist = input("Enter Artist Name ")

# Search for music by artist
x = musicbrainzngs.search_releases(artist="" + artist, country="GB", status="Offical", format='CD')

# Takes 5 random songs from the x variable seach.
for i in range(5):
    xx = x['release-list'][songNumber[n]]['title']
    songslist.append(xx)
    n += 1
    
n = 0

# Takes Songs and inputs them in the request api and then lyric word count is added to countlist.
if i in range(5):
    song = json.dumps(songslist[n])
    request = Request('https://api.lyrics.ovh/v1/' + artist.replace(" ", "%20") + '/' + song.replace(" ", "%20"))
    response_body = urlopen(request).read()         # Returns byte value
    response_body = str(response_body, 'utf-8')     # Coverts byte to string
    response_body = ast.literal_eval(response_body) # Converts String to Dict
    response_body = response_body['lyrics']         # Gets the Dict Lyrics value 
    response_body = str(response_body)              # converts back to string
    res = len(response_body.split())
    countlist.append(res)
    n += 1

for x in range(len(countlist)): 
    print countlist[x], 

# Results
print("\n")
print('The Average wordcount of ' + artist + ' from 5 songs is ' + str(statistics.mean(countlist)))
print("\n")
print('The Following Songs have been compared:')

# List songs along with word count used in Calculations
n = 0
for i in range(5):
    print(songslist[n] + ': ' + str(countlist[n]))
    n += 1