import streamlit as st
from yt_dlp import YoutubeDL
import os

st.title("YouTube Video Downloader")

video_url = st.text_input("Paste YouTube Video URL")

if video_url:

    st.video(video_url)

    if st.button("Download Video"):

        try:

            ydl_opts = {
                'format': 'best',
                'outtmpl': 'video.%(ext)s',
                'noplaylist': True,
                'quiet': True,
            }

            with YoutubeDL(ydl_opts) as ydl:

                info = ydl.extract_info(video_url, download=True)

                filename = ydl.prepare_filename(info)

            st.success("Download Completed")

            with open(filename, "rb") as file:

                st.download_button(
                    label="Save Video",
                    data=file,
                    file_name=os.path.basename(filename),
                    mime="video/mp4"
                )

        except Exception as e:

            st.error("Video download failed")
            st.write(e)
