import re
import requests
import itertools

r = requests.get('https://music.yandex.ru/users/kdkulakov/tracks')
regex_artist = r'"artists":\[{"id":[0-9]+,"name":"[a-zA-Zа-яА-Я\s.ё\'"]+'
regex_song = r'"realId":"[0-9]+","title":"[a-zA-Zа-яА-Я\s.ё\'"]+'
test_str = r.text

songs = re.finditer(regex_song, test_str)
artists = re.finditer(regex_artist, test_str)

for matchNum, match in enumerate(songs):
    matchNum = matchNum + 1

    print ("{match}".format(match = match.group()))
#    for artistNum, art in enumerate(artists):
#        ertistNum = artistNum + 1
#        print ("{art}".format(art = art.group())