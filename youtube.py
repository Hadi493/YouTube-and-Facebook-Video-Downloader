from pytube import YouTube, Playlist
import os

def clear_screen():
    # This function clears the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def downloadPlaylist(link):
    directory = "/home/hadi/Videos/DownloadYT"
    clear_screen()
    try:
        playlist = Playlist(link)
        count = 0
        for video in playlist.videos:
            video_title = video.title
            count += 1
            video_title = f'{count}. {video_title}.mp4'
            print("Downloading... : " + video_title)
            video.streams.get_highest_resolution().download(output_path=directory, filename=video_title)
            print("Download Completed!")

        print("DOWNLOADED THE FULL PLAYLIST!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def downloadVideo(link):
    directory = "/home/hadi/Videos/DownloadYT"
    clear_screen()
    try:
        video = YouTube(link)
        video_title = video.title
        print("Downloading... : " + video_title)
        video.streams.get_highest_resolution().download(output_path=directory)
        print("Download Completed!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Example usage:
# downloadPlaylist("playlist_link_here")
# downloadVideo("video_link_here")
