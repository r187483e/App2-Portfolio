import streamlit as st
import pandas

st.title("The Best Company")
content = """
In this unit I use the word Methodology as a general term to cover whatever you decide to include in the chapter
 where you discuss alternative methodological approaches, justify your chosen research method, and describe the 
 process and participants in your study.
"""
st.write(content)
st.subheader("Our Team")

col1, empty_col, col2,empty_col2, col3 = st.columns([4,1,4,1,4])
df = pandas.read_csv("project/data.csv", sep=",")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("project/images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("project/images/" + row["image"])


with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("project/images/" + row["image"])




