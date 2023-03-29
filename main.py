from pytube import YouTube

link = "https://youtu.be/b5WdL51te0A"
my_video = YouTube(link)

# Getting video title
print(my_video.title)

# Getting url thumbnail
#print(my_video.thumbnail_url)

# getting streams
print(my_video.streams.filter(progressive=True))

