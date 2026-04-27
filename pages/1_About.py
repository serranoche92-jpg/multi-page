import streamlit as st

st.snow()  # ❄️ effect at top

st.markdown("<h1 style='text-align: center;'>👤 About Me</h1>", unsafe_allow_html=True)

st.markdown("---")

st.info("✨ Welcome to my personal profile page!")

col1, col2 = st.columns(2)

with col1:
    st.success("Name: AS SERRANO. SAN PASCUAL")
    st.success("Course: 3rd Year BSCS")
    st.success("School: DEBESMSCAT")
    st.success("Email: serranoche92@gmail.com")

with col2:
    st.warning("""
💡 Skills:
- Cooking  
- Cleaning  
- Communication  
- Writing stories
""")

st.markdown("---")

st.write("### 🎯 Goals")
st.write("""
I want to graduate, finish my studies, and have a good life.  
I also want to support and spoil my parents ❤️
""")

st.markdown("🔗 Facebook: [Visit my profile](https://facebook.com/sanpascual122704)")