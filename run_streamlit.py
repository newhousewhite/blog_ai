import streamlit as st
from main import BlogWriter
from search import GoogleSearch


@st.cache_resource
def prep_writer():
    return BlogWriter()

@st.cache_resource
def prep_search():
    return GoogleSearch()

# create class objects
blog = prep_writer()
search = prep_search()


# Title of the Streamlit app
st.title("블로지니")

# Create tabs
tab_text, tab_image, tab_ent, tab_search = st.tabs(["텍스트", "이미지", "엔터", "블로그 검색"])

text_input = ""
# 텍스트 생성
with tab_text:
    output = st.empty()
    text_input_text = st.text_area("블로그 텍스트", height=300, key="text")
    button_title = None
    button_tags = None
    button_critic = None
    cols = st.columns([1, 1, 1, 3])
    with cols[0]:
        button_title = st.button("제목")
    with cols[1]:
        button_tags = st.button("태그")
    with cols[2]:
        button_critic = st.button("평가")

# 이미지 생성
with tab_image:
    output = st.empty()
    text_input_image = st.text_input("이미지 설명 텍스트", key="image")
    button_image = None
    cols = st.columns([2, 5])
    with cols[0]:
        button_image = st.button("이미지 만들기")

# 온라인 검색
with tab_search:
    output = st.empty()
    cols = st.columns([3, 5, 2])
    with cols[0]:
        text_input_url = st.text_input("플랫폼 URL", key="platform_url")
    with cols[1]:
        text_input_search = st.text_input("블로그 검색어 텍스트", key="search")
    button_search = None
    cols = st.columns([2, 5])
    with cols[0]:
        button_search = st.button("검색")

# 엔터
with tab_ent:
    output = st.empty()
    text_input_ent = st.text_area("블로그 텍스트", height=300, key="ent")
    cols = st.columns([1, 1, 1, 2, 3])
    with cols[0]:
        button_hiphop = st.button("힙합")
    with cols[1]:
        button_classic = st.button("한시")
    with cols[2]:
        button_bossy = st.button("꼰대")
    with cols[3]:
        button_idiom = st.button("사자성어")

# Actions when buttons are clicked
out_type = None
input_data = None
if button_title:
    out_type = "title"
    input_data = text_input_text
if button_image:
    out_type = "image"
    input_data = text_input_image
if button_tags:
    out_type = "tags"
    input_data = text_input_text
if button_critic:
    out_type = "critic"
    input_data = text_input_text
if button_hiphop:
    out_type = "hiphop"
    input_data = text_input_ent
if button_classic:
    out_type = "classic"
    input_data = text_input_ent
if button_bossy:
    out_type = "bossy"
    input_data = text_input_ent
if button_idiom:
    out_type = "idiom"
    input_data = text_input_ent
if button_search:
    out_type = "search"
    input_data = " ".join((text_input_search, text_input_url))


if out_type:
    if not input_data:
        print("input_data is empty")

    if button_image:
        image_url = blog.run(input_data, out_type)
        output = st.empty()
        st.image(image_url, caption=input_data, use_column_width=True)
    elif button_title or button_tags or button_critic or button_hiphop or button_classic or button_bossy or button_idiom:
        out_text = blog.run(input_data, out_type)
        output = st.empty()
        output.write(out_text)
    elif button_search:
        num_results = 10
        results_orig = search.get_google_results(input_data, num_results*10)
        results = search.search_url_filter(results_orig, text_input_url, num_results)
        links = search.get_hyperlinks(results)

        for id, anchor_text, url in links:
            st.markdown(f"[{id}: {anchor_text}]({url})")
