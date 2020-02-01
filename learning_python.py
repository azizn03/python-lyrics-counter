#!/usr/bin/python
#variable assigment:

from urllib.request import Request, urlopen
import musicbrainzngs
import random
nn = 5
n = 0
songslist = []
list=[]
for i in range(nn):
    r=random.randint(1,20)
    if r not in list: 
        list.append(r)
        nn += 1


print(list)
musicbrainzngs.set_useragent("LyricsWordCount", "1.0", "azizn03",)
#musicbrainzngs.set_hostname("musicbrainz.org", use_https=False)

artist = input("Enter Artist Name ")

result = musicbrainzngs.search_artists(artist="" + artist, type="group", country="GB")

artistid = result['artist-list'][0]['id']

x = musicbrainzngs.browse_releases(artist="" + str(artistid), country="GB")

for i in range(5):
    print(x['release-list'][list[n]]['title'])
    n += 1
    songslist.append(x)
    # for i in range(10):
    #       r=random.randint(1,100)
    #       if r not in list: list.append(r)
#print(x)
#recording-list

for y in songslist:
  print(y)


#for artist in result['artist-list']:
#    print("{name}: {id}".format(name=artist["name"], id=artist['id']))


# artist = input("Enter Artist Name ")
# song = input ("Enter Song Name ")
# request = Request('https://api.lyrics.ovh/v1/' + artist.replace(" ", "%20") + '/' + song.replace(" ", "%20"))










#result['artist-list'][id]
# print(result)
# {'artist-list': [{'id': 'cc197bad-dc9c-440d-a5b5-d52ba2e14234', 
# 'type': 'Group', 
# 'ext:score': '100', 
# 'name': 'Coldplay', 
# 'sort-name': 'Coldplay', 
# 'country': 'GB', 'area': {'id': '8a754a16-0027-3a29-b6d7-2b40ea0481ed', 
# Dictionary synax 
#my_dict {'key1':'value1','key2':'value2'}



# x = musicbrainzngs.get_artist_by_id("cc197bad-dc9c-440d-a5b5-d52ba2e14234", includes=["releases"], release_status=[], release_type=[])

# xx = x["releases"]
# print(xx)

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]
# print(x)








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

# grabbing array values

# i.e.

# "folowers": {
#     "href": null,
#     "total": 21
# },

# followers = user['followers']['total']

# b = b['lyrics']
# https://search.azlyrics.com/search.php?q=Coldplay&w=songs&p=2
# href="https:\/\/www.azlyrics\.com\/lyrics\/coldplay\/[a-z]+\.html"
# asd href="https://www.azlyrics.com/lyrics/coldplay/sparks.html" qweqwe
