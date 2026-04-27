import streamlit as st
import time

st.set_page_config(page_title="My Portfolio App", layout="centered")

st.markdown("<h1 style='text-align: center;'>👋 Welcome to My Portfolio</h1>", unsafe_allow_html=True)

st.markdown("---")

st.write("Hi! This is my personal Streamlit multipage website.")

name = st.text_input("Enter your name:")

if st.button("Greet Me"):
    st.success(f"Hello {name}! Welcome 😊")

    # 🎉 EFFECT
    st.balloons()

st.markdown("---")

# 📊 Fake loading effect
st.write("Loading my profile...")
progress = st.progress(0)

for i in range(100):
    time.sleep(0.01)
    progress.progress(i + 1)

st.success("Profile loaded successfully 🚀")