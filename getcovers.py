#/usr/bin/env python3
import os
import pylast
import shutil
import subprocess
import random
import re
from config import musicdir
from getplaylistalbums import get_album_paths
from agfunctions import connect_client, get_key
import requests

def get_local_art(songdir):
    theimages = []
    if songdir.endswith('cue'):
        songdir = songdir.rsplit('/',1)[0]
    if songdir.endswith('zip'):
        get_lastfm_art(network, client)
        return
    for fname in os.listdir(songdir):
        if fname.endswith(('.png','.jpg','.jpeg','gif')):
            theimages.append(songdir + "/" + fname)
    if theimages:
        biggestimage = max(theimages, key=os.path.getsize)
        subprocess.call(['convert', '-resize', '200x200', biggestimage, 'cover.png'])
        print("local image written to covergrid/cover.png")
    else:
        print("no local art, checking lastfm...")
        get_lastfm_art(songdir)

def get_lastfm_art(songdir):
    for fname in os.listdir(songdir):
        if fname.endswith(('.flac','.mp3','.aac','wav')):
            firstsong = songdir + "/" + fname
            print(firstsong)
            break

    myexifdump = subprocess.check_output(['exiftool', firstsong]).decode("utf-8")
    for i in myexifdump.split('\n'):
        if re.search('Artist                          :', i):
            artist = i.split(':')[1]
        #else:
        #    artist = 'Primate'
        if re.search('Album                           :', i):
            album = i.split(':')[1]
        #else:
        #    album = 'Greatest Hits'

    print("Artist: " + artist)
    print("Album: " + album)


    fmalbum = network.get_album(artist, album)
    print("fmalbum: ")
    print(fmalbum)
    try:

        url = fmalbum.get_cover_image().encode("utf-8")
        response = requests.get(url, stream =True)

        if response.status_code == 200:
            with open('cover.png', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            subprocess.call(['convert', '-resize', '200x200', 'cover.png', 'cover.png'])
            del response
        print("Last.fm image written to cover.png")
    except:
        print("couldn't find a cover at last.fm, either.")
        enjoy_monkey()

def enjoy_monkey():
    print("Enjoy monkey.")
    monkeydir = "/endo/pics/monkeys"
    monkey= monkeydir + "/" +random.choice(os.listdir(monkeydir))
    subprocess.call(['convert', monkey, '-resize', '200x200^', '-gravity',
                     'center','-extent', '200x200', 'cover.png'])

client = connect_client()
network = pylast.LastFMNetwork(get_key())
albumPaths = get_album_paths(client)

mytoken = 1
#for i in albumPaths:
#    print('bazinga ' + str(mytoken))
#    mytoken = mytoken + 1
#
for albumpath in albumPaths:
    if mytoken < 17:
        get_local_art(albumpath)
        subprocess.call(['mv', 'cover.png', 'index16/cover' + str(mytoken).zfill(4) + '.png'])
        mytoken= mytoken + 1
    else:
        break
