from song import *
import youtube_dl
import re
import urllib.request
import urllib.parse
import pafy
import os
import shutil

SONGSFOLDER = "song_downloads"

if os.path.exists(SONGSFOLDER):
    shutil.rmtree(SONGSFOLDER)
os.mkdir(SONGSFOLDER)

def get_url(song_name, artist):
    keyword = song_name.replace(" ", "+") + "+by+" + artist.replace(" ", "+")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + keyword) #can look at meta data and see if it displays the length of the video and check that with information given by user
    vid_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    url = "https://www.youtube.com/watch?v=" + vid_ids[0]
    return url

def download_audio(url, song):
    song_name = song.get_name()
    video = pafy.new(url)
    length = video.length
    song.set_length(length)
    bestaudio = video.getbestaudio(preftype='m4a')
    extension = bestaudio.extension
    song.set_extension(extension)
    filename = song_name.replace(" ", "_") + '.' + extension
    song.set_filename(filename)
    bestaudio.download(filepath= os.getcwd() + "\\" + SONGSFOLDER + "\\" + filename)
    

    # bestaudio = video.getbestaudio()
    # print(bestaudio)



def download_song(song):
    url = get_url(song.get_name(), song.get_artist())
    download_audio(url, song)
    print(song.get_filename())
    print(song.get_name())
    return True

        
