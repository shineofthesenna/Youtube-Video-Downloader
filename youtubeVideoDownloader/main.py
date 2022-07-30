
# Importing the module
import pytube

# Taking input the link

link = input('Paste the url here : ')

# Using the module to download the video

video = pytube.YouTube(link)
video.streams.first().download()

# to make sure that the download is complete

print("Downloaded Successfully, ", link)