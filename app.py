import os
import re
from pytube import Playlist, YouTube
import streamlit as st 
from streamlit_option_menu import option_menu

# from tqdm import tqdm
# from main import playlist_download,download_one
import os

# # Function to download YouTube video
# def download_youtube_video(youtube_url, save_path):
#     st.write("Downloading...")
#     yt = YouTube(youtube_url, on_progress_callback=on_progress)
#     stream = yt.streams.get_audio_only()  # Get the audio stream
#     stream.download(output_path=save_path)
#     st.write("Download completed.")

# # Callback function to update the progress bar
# def on_progress(stream, chunk, remaining):
#     total_size = stream.filesize
#     bytes_downloaded = total_size - remaining
#     progress_bar.progress(bytes_downloaded / total_size)


def playlist_down(playlist_url):
    # playlist_url = "https://www.youtube.com/playlist?list=PLnCSU2kELkG1b0T8TCdRRPI9HVBcrlyJD"
    playlist = Playlist(playlist_url)
    playlist_name = re.sub(r'\W+', '-', playlist.title)
    st.write(playlist_name) 

    ## Creating Songs folder paths
    if not os.path.exists(playlist_name):
        os.mkdir(playlist_name)
        
    for index, v in enumerate(playlist.videos, start=1):
        video = YouTube(v.watch_url, use_oauth=True,allow_oauth_cache=True)
        video_resolution = video.streams.filter(only_audio=True).first()
        video_filename = f"{video_resolution.default_filename}"
        
        ## Check if that songs are already presents or not
        video_path = os.path.join(playlist_name, video_filename)
        if os.path.exists(video_path):
            print(f"{video_filename} already exists")
            continue
        audio_stream = video.streams.get_audio_only()
        st.write(f"Downloading audio for {video_filename}")
        audio_stream.download(filename=f"{video_path}")
    st.write('above code ran successfully!!!!!!!!!!!!!!!!!!!!')
    
def download_one(video_url):
    video = YouTube(video_url,use_oauth=True,allow_oauth_cache=True)
    video_resolution = video.streams.filter(only_audio = True).first()
    video_filename = f"{video_resolution.default_filename}"

    audio_stream = video.streams.get_audio_only()
    st.write(f"Downloading audio for {video_filename}")
    try:
        audio_stream.download(filename=f"{video_filename}")
    except:
        st.write(f'Failed to download {video_filename}!!!!!')

    st.write("audio was downloaded successfully") 


# Main function
def main():
    # st.title("YouTube Downloader")
    selected = streamlit_menu()
    
    if selected == "Playlist link":
        # Input box for YouTube URL
        youtube_url = st.text_input("Enter YouTube Playlist URL:")
        # Download button
        if st.button("Download"):
            if youtube_url:
                playlist_down(youtube_url)

    
    if selected == "Video link":
        # Input box for YouTube URL
        youtube_url = st.text_input("Enter YouTube single Video URL:")
        # Download button
        if st.button("Download"):
            if youtube_url:
                download_one(youtube_url)
#


    # # Input box for download path
    # download_path = st.text_input("Enter download path (Leave empty for default 'downloads' folder):")


    



def streamlit_menu():
    # 2. horizontal menu with custom style
    selected = option_menu(
        menu_title='Youtube Audio Downloader',  # required
        options=["Playlist link", "Video link"],  # required
        icons=["music-note-list","music-note-beamed"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal"
        # styles={
        #     "container": {"padding": "0!important", "background-color": "#fafafa"},
        #     "icon": {"color": "orange", "font-size": "25px"},
        #     "nav-link": {
        #         "font-size": "25px",
        #         "text-align": "center",
        #         "margin": "0px",
        #         "--hover-color": "#eee",
        #     },
            
        # },
    )
    return selected




#  App entry point
if __name__ == "__main__":
    main()
