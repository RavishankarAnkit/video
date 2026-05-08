import streamlit as st

st.title("Online Video Player")

video_url = st.text_input("Paste Video URL")

if video_url:

    st.success("Video Loaded")

    st.video(video_url)
