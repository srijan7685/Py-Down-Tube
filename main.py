from pytube import YouTube

link = input("Enter the link:\n>> ")
my_video = YouTube(link)

# Getting video title
print(my_video.title)
