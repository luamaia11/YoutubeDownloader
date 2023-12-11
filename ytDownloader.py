from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("title: ", yt.title)

print("View: ", yt.views)

yd =  yt.streams.get_highest_resolution()

yd.download(yd.download(yd.download('C:\\Users\\lua_m\\Music\\musicapython\\')
))

