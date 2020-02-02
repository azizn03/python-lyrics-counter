#!/usr/bin/python
#variable assigment:

from urllib.request import Request, urlopen
import musicbrainzngs
import random
import json 
import ast
import statistics # calculating the mean value
# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.htm")

# @app.route('/', methods=['POST'])
# def my_form_post():
#     text = request.form['text']
#     artist = text
#     return artist

# artist = my_form_post()

songslist = []
countlist = []
listt=[]
n = 0
xx = 0
r=random.sample(range(16), 5)

for i in range(5):
    listt.append(r[xx])
    xx += 1

print(listt)
musicbrainzngs.set_useragent("LyricsWordCount", "1.0", "azizn03",)

artist = input("Enter Artist Name ")

x = musicbrainzngs.search_releases(artist="" + artist, country="GB", status="Offical", format='CD')

for i in range(5):
    xx = x['release-list'][listt[n]]['title']
    songslist.append(xx)
    n += 1
    
n = 0

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


print('The Average wordcount of ' + artist + 'from 5 songs are ' + statistics.mean(countlist))
print("\n")
print('The Following Songs have been compared:')
n = 0
for i in range(5):
    print(songslist[n]
    n += 1

# if __name__ == "__main__":
#     app.run(host='0.0.0.0')