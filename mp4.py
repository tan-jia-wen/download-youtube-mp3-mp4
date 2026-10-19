import os
import yt_dlp

os.makedirs("Downloaded", exist_ok=True)

a = input("Enter URL: ")

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': 'Downloaded/%(title)s.%(ext)s',  # save inside Downloaded folder
    'merge_output_format': 'mp4',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([a])