import streamlit as st
from main import BlogWriter


@st.cache_resource
def prep():
    return BlogWriter()

blog = prep()

# Title of the Streamlit app
st.title("블로그 글쓰기 AI")

# Instructions
st.write("Enter a long-form text in the box below, and click one of the buttons to process it.")

# Text area for long-form text input
long_text = st.text_area("Input Text", height=300)

# Create buttons
button_title = None
button_tags = None
button_critic = None
button_hiphop = None
cols = st.columns([1, 1, 1, 1, 2])
with cols[0]:
    button_title = st.button("타이틀")
with cols[1]:
    button_tags = st.button("태그")
with cols[2]:
    button_critic = st.button("평가")
with cols[3]:
    button_hiphop = st.button("힙합")

# Placeholder for the output
output = st.empty()


# Actions when buttons are clicked
out_type = None
if button_title:
    out_type = "title"
if button_tags:
    out_type = "tags"
if button_critic:
    out_type = "critic"
if button_hiphop:
    out_type = "hiphop"


if out_type:
    out_text = blog.run(long_text, out_type)
    output.write(out_text)


