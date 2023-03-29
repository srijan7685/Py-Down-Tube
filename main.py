from pytube import YouTube
import pyperclip
print("Go & Copy Your Link First !!!")
link = pyperclip.waitForNewPaste()
print("Your Song Title:")
print("_"*40)
video = YouTube(link)
print(video.title)
correct = input("Proceed ? (y / n):\n>> ").lower()
if correct == "y":
    stream = video.streams.get_highest_resolution()
    stream.download()