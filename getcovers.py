#/usr/bin/env python3
import os
import pylast
import shutil
import subprocess
import random
from config import musicdir
from getplaylistalbums import get_album_paths
from agfunctions import connect_client, get_key

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
        subprocess.call(['convert', '-resize', '400x400', biggestimage, 'cover.png'])
        print("local image written to artgrabber/cover.png")
    else:
        get_lastfm_art(network, client)

def get_lastfm_art(network, client):
    try:
        album = network.get_album(client.currentsong()['artist'],
                                  client.currentsong()['album'])
    except:
        album = "greatest hits"
    try:

        url = album.get_cover_image().encode("utf-8")
        response = requests.get(url, stream =True)

        if response.status_code == 200:
            with open('cover.png', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            subprocess.call(['convert', '-resize', '400x400', 'cover.png', 'cover.png'])
            del response
        print("Last.fm image written to cover.png")
    except:
        print("couldn't find a cover at last.fm, either.")
        enjoy_monkey()

def enjoy_monkey():
    print("Enjoy monkey.")
    monkeydir = "/endo/pics/monkeys"
    monkey= monkeydir + "/" +random.choice(os.listdir(monkeydir))
    subprocess.call(['convert', '-resize', '400x400', monkey, 'cover.png'])

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
        subprocess.call(['mv', 'cover.png', 'index16/cover' + str(mytoken) + '.png'])
        mytoken= mytoken + 1
    else:
        break
