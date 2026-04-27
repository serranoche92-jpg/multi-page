import streamlit as st

st.markdown("<h1 style='text-align: center;'>📬 Contact Me</h1>", unsafe_allow_html=True)

st.markdown("---")

name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

if st.button("Send Message"):
    if name and email and message:
        st.success("Message sent successfully! 🎉")
        st.balloons()
    else:
        st.error("Please fill all fields 😅")