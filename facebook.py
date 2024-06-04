import subprocess
import youtube_dl
import clearScreen as c

def fbVideoDownload(link):
    c.clear_screen()
    print("Is it a public video?")
    print("1. Yes")
    print("2. No")
    res = input().strip()

    if res not in ['1', '2']:
        print("Invalid input. Please enter 1 for Yes or 2 for No.")
        return

    try:
        c.clear_screen()
        if res == '1':
            print("Downloading ...")
            # Set the download directory to /home/hadi/Videos/DownloadYT
            ydl_opts = {
                'outtmpl': '/home/hadi/Videos/DownloadYT/%(title)s.%(ext)s'
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            print("Download Complete!")
        else:
            print("Private videos can't be downloaded in this version.")
    except Exception as e:
        print(f"There was an error: {e}. Please run the program again.")

# Example usage
link = "https://www.facebook.com/example_video_link"
fbVideoDownload(link)
