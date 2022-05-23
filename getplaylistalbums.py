#!/usr/bin/env python3
import mpd
import os
from config import musicdir

def connect_client():
    """Connect to MPD Client"""
    client = mpd.MPDClient()
    client.connect("localhost", 6600)
    return client

client = connect_client()

def get_album_paths(client):
    albumPaths = []
    for song in client.playlistinfo():
        songfile = (song["file"])
        songdir = os.path.dirname(os.path.join(musicdir,songfile))
        if len(albumPaths) == 0:
            albumPaths.append(songdir)
        elif albumPaths[-1] != songdir:
            albumPaths.append(songdir)
    return albumPaths

client = connect_client()
albumPaths = get_album_paths(client)
#print(albumPaths)
