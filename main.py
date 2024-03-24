import os
import re
from pytube import Playlist, YouTube
print('Songs Downloaded from Youtube')


def playlist_download(playlist_url):
    # playlist_url = "https://www.youtube.com/playlist?list=PLnCSU2kELkG1b0T8TCdRRPI9HVBcrlyJD"
    playlist = Playlist(playlist_url)
    playlist_name = re.sub(r'\W+', '-', playlist.title)
    print(playlist,playlist_name) 

    ## Creating Songs folder paths
    if not os.path.exists(playlist_name):
        os.mkdir(playlist_name)
        
    for index, v in enumerate(playlist.videos[1:2], start=1):
        video = YouTube(v.watch_url, use_oauth=True,allow_oauth_cache=True)
        video_resolution = video.streams.filter(only_audio=True).first()
        video_filename = f"{video_resolution.default_filename}"
        
        ## Check if that songs are already presents or not
        video_path = os.path.join(playlist_name, video_filename)
        if os.path.exists(video_path):
            print(f"{video_filename} already exists")
            continue
        audio_stream = video.streams.get_audio_only()
        print(f"Downloading audio for {video_filename}")
        try:
            audio_stream.download(filename=f"{video_path}")
        except:
            print(f'Failed to download {video_filename}!!!!!')
    print('All the above files were downloaded successfully')
   
   
def download_one(video_url):
    video = YouTube(video_url,use_oauth=True,allow_oauth_cache=True)
    video_resolution = video.streams.filter(only_audio = True).first()
    video_filename = f"{video_resolution.default_filename}"

    audio_stream = video.streams.get_audio_only()
    print(f"Downloading audio for {video_filename}")
    try:
        audio_stream.download(filename=f"{video_filename}")
    except:
        print(f'Failed to download {video_filename}!!!!!')

    print("audio was downloaded successfully") 
    
playlist_download("https://www.youtube.com/playlist?list=PLnCSU2kELkG1b0T8TCdRRPI9HVBcrlyJD")