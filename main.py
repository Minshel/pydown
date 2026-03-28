import yt_dlp

fmt_choice = input("Enter format (mp4 or mp3) or 'exit': ").strip().lower()
        
if fmt_choice not in ["mp4", "mp3"]:
    print("Invalid format!")

url = input("Enter Youtube Video URL: ")

if fmt_choice == "mp4":
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'ffmpeg_location': './',
        'merge_output_format': 'mp4',
    }
else:  # mp3
    ydl_opts = {
        'format': 'bestaudio/best',
        'ffmpeg_location': './',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Success!")
except Exception as e:
    print(f"Error: {e}")