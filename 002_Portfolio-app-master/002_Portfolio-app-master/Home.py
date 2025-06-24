import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg")

with col2:
    st.title("Elisa Suárez")
    content = """
    Hi there! I´m a Data Scientist and a Data Analyst. I graduated from Coderhouse in March 2023. 
    I'm currently studying to be a Data Engineer as well, and also I'm doing the "Mathematics for Machine Learning 
    and Data Science" specialization by IBM.
    
    I speak Spanish as my mother tongue, English as a second language (C1 level) and I'm currently attending Portuguese lessons (B1 level).
    
    I'm always looking to learn new skills, take on extra responsibilities, and grow professionally. 
    """
    st.info(content)

content_below = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content_below)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")  # poner link Github

