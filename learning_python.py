#!/usr/bin/python
#variable assigment:

from urllib.request import Request, urlopen
import musicbrainzngs
import random
import json 

songslist = []

list=[]
n = 0
xx = 0
r=random.sample(range(16), 5)
for i in range(5):
    list.append(r[xx])
    xx += 1

print(list)
musicbrainzngs.set_useragent("LyricsWordCount", "1.0", "azizn03",)

artist = input("Enter Artist Name ")

x = musicbrainzngs.search_releases(artist="" + artist, country="GB", status="Offical", format='CD')

for i in range(5):
    print(x['release-list'][list[n]]['title'])
    n += 1
    songslist.append(x)
    
song = json.dumps(songslist[1])
print(song)
request = Request('https://api.lyrics.ovh/v1/' + artist.replace(" ", "%20") + '/' + song.replace(" ", "%20"))


response_body = urlopen(request).read()
print(response_body)




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


