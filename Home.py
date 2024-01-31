import streamlit as st
import pandas


col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with (col2):
    st.title("Alvinah Singano")
    content = """
    (A highly energetic and hardworking graduate from University of Zimbabwe 
    (UZ) with (BSc)Honors Degree in Computer Science with knowledge in Information
    and Technology, Networking, Software and Web designing. Also, 
    I obtained a networking HUAWEI certificate in Datacom (HCIA)
    """

    st.info(content)

content1 = """
Below you can find some of the apps i have built in python, Feel free to contact me!
"""
st.write(content1)

col3, empty_col,col4 = st.columns([1.5, 0.5, 1.5])
# df=dataframe
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


