import os
import yt_dlp

os.makedirs("Downloaded", exist_ok=True)

a = input("Enter URL: ")

ydl_opts = {
    'format': 'best',
    'outtmpl': 'Downloaded/%(title)s.%(ext)s',  # save inside Downloaded folder
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([a])