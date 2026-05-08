import streamlit as st
import vlc
import time

st.title("VLC Video Player")

video_url = st.text_input("Paste Video URL")

if st.button("Play Video"):

    if video_url:

        st.success("Playing Video in VLC...")

        player = vlc.MediaPlayer(video_url)

        player.play()

        time.sleep(1)

        st.write("Video Started")

    else:
        st.error("Please enter a video URL")
