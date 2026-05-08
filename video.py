import streamlit as st
from yt_dlp import YoutubeDL

st.title("YouTube Video Downloader")

# Video URL
video_url = st.text_input("Paste YouTube Video URL")

if video_url:

    st.video(video_url)

    if st.button("Download Video"):

        ydl_opts = {
            'format': 'mp4',
            'outtmpl': 'downloaded_video.%(ext)s',
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        video_file = open("downloaded_video.mp4", "rb")

        st.success("Video Downloaded")

        st.download_button(
            label="Click Here to Save Video",
            data=video_file,
            file_name="video.mp4",
            mime="video/mp4"
        )
