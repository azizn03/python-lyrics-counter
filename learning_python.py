#!/usr/bin/python
#variable assigment:

from urllib.request import Request, urlopen
import musicbrainzngs
import random
import json 
import ast
import statistics # calculating the mean value
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
    print(x['release-list'][list[n]]['title'])
    xx = x['release-list'][list[n]]['title']
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


print(statistics.mean(countlist))

# x = musicbrainzngs.get_artist_by_id("cc197bad-dc9c-440d-a5b5-d52ba2e14234", includes=["releases"], release_status=[], release_type=[])

# xx = x["releases"]
# print(xx)


# print(response_body)
# print(type(response_body))
# print(response_bodyy)

# intvalue = 3
# print(intvalue)
# print(type(intvalue))

# math1 = 2
# math2 = 3
# math3 = math1 * math2
# print(math3) 

# #indexing

# firststring = "hello world"
# print(firststring[9])
# print(firststring[-2])
# print(firststring[:5])
# print(firststring[6:])
# print(firststring[::2])
# print(firststring[::-2])

# # list stuff from character
# # output songs into array
# # for ( array < 0; i++)
# #  execute 

# # wordtotal / countstuff = total word count.


# #I/O files 
# f= open("file1.txt", "w+") # creates file with read/write permissions

#Takes user input for name
# name = input('what is your name ')
# favorite_colour = input('Favorite colour? ')
# print('Hi ' + name)
# print (name + ' likes ' + favorite_colour)

# Converting from string to int

# birth_year = input('Birth year: ')
# print(type(birth_year))
# agenumber = input('age: ')
# age = int(agenumber) - int(birth_year) #converts birth_year string value to int so it can be subtracted from age.
# print(age)

#Function to count letters in a string
# course = "python for beginners"
# print(len(course))
# print(course.upper())


# followers = user['followers']['total']


