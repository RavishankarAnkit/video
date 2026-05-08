import streamlit as st
import requests

st.title("Online Video Player and Downloader")

# Input video URL
video_url = st.text_input("Paste Video URL")

if video_url:

    st.success("Video Loaded")

    # Play video
    st.video(video_url)

    # Download button
    try:

        response = requests.get(video_url)

        st.download_button(
            label="Download Video",
            data=response.content,
            file_name="video.mp4",
            mime="video/mp4"
        )

    except:
        st.error("Unable to download this video")
