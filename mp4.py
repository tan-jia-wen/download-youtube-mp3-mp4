import yt_dlp

a = input("Enter URL: ")

ydl_opts = {
    'format': 'best',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([a])