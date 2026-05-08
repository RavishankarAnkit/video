import streamlit as st
from yt_dlp import YoutubeDL
import os
import uuid

st.title("YouTube Video Downloader")

video_url = st.text_input("Paste YouTube URL")

if video_url:

    st.video(video_url)

    if st.button("Download Video"):

        try:

            # Unique filename
            unique_id = str(uuid.uuid4())

            ydl_opts = {
                'format': 'best',
                'outtmpl': f'{unique_id}.%(ext)s',
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

            st.error("Download Failed")
            st.write(e)
