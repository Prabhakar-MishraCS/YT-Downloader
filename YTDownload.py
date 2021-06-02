import time
import os
import shutil
from pytube import YouTube

url =YouTube("https://www.youtube.com/watch?v=fijsOsEf-jg&t=6s")

vid = url.streams.get_highest_resolution()
vid.download()

#********************************************

source ="/Users/prabhms/PycharmProjects/YTDownloader"
destination = "/Users/prabhms/Desktop/PrabhuCSYT"
sourcefile = os.listdir(source)

for file in sourcefile:
    if file.endswith(".mp4"):
        shutil.move(os.path.join(source,file), os.path.join(destination,file))