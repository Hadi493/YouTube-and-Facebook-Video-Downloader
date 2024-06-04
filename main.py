import os
import youtube as y
import facebook as f
import clearScreen as c

print("What do you want to download?")
print("\t1. Youtube Video")
print("\t2. Youtube Playlist")
print("\t3. Facebook Video")

type = input()

c.clear_screen()

# Change Directory
path = "./videos/"
if not os.path.exists(path):
    os.makedirs(path)
    os.chdir(path)

link = input("Give the link of: ")

if(type == '1'):
    y.downloadVideo(link)
if(type == '2'):
    y.downloadPlaylist(link)
if(type == '3'):
    f.fbVideoDownloard(link)