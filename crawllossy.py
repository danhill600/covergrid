#!/usr/bin/env python3
from agfunctions import network, get_lastfm_art, connect_client, get_key
import pylast
import subprocess
import os
import re


rootDir = '/endo/lossy'
myDirs = []
for dirName, subdirList, fileList in os.walk(rootDir):
   myDirs.append(os.path.join(rootDir,dirName))

#print(myDirs)
ext = [".png", ".jpg", ".PNG", ".JPG",".jpeg", ".JPEG"\
       ".gif",".GIF"]
picturelessDirs = []

for aDir in myDirs:
    for fname in os.listdir(aDir):
       if fname.endswith(tuple(ext)):
           break
    else:
        picturelessDirs.append(os.path.join(rootDir,aDir))

#print(picturelessDirs)

token=1
for songdir in picturelessDirs:
   # print(bDir)
   if token < 17:
      print(songdir)
      if get_lastfm_art(songdir)=='funkywinkerbean':
         subprocess.call(['cp', 'cover.png', '/var/www/lighttpd/grid/grid' + str(token).zfill(4) + '.png'])
         token=token+1
   else:
      break
