import os.path
from pytube import YouTube
import pyperclip

print("Go & Copy Your Link First !!!")
link = pyperclip.waitFornPaste()
print("Your Song Title:")
print("_"*100)
video = YouTube(link)
print(video.title)
print("_"*100)
correct = input("Proceed ? (y / n):\n>> ").lower()
if correct == "y":
    dir = input("Choose Your Directory To Save Video:\n>> ")
    stream = video.streams.get_highest_resolution()
    output = stream.download()
    video_path = os.path(dir, output)
    final_video = open(video_path, "w")