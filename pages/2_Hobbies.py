import streamlit as st

st.markdown("<h1 style='text-align: center;'>🎮 My Hobbies</h1>", unsafe_allow_html=True)

st.markdown("---")

hobby = st.selectbox(
    "Choose a hobby:",
    ["Drawing", "Reading Books", "Reading Manhwa", "Writing Stories"]
)

st.success(f"I love {hobby} ❤️")

if st.button("Show Fun Effect"):
    st.balloons()

st.info("Relaxing activities help me stay creative ✨")