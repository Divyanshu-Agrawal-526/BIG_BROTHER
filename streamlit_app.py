import streamlit as st
from st_functions import st_button, load_css
from PIL import Image
import mysql.connector

load_css()

st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.jpeg'))

st.header('BIG BROTHER')

st.header('SACRED EYE')

st.info('Developed by Akshat Singh Jaiswal, Vyoman Jain, Aditya Naskar and Divyanshu Agrawal')

icon_size = 20

st_button('webcam', 'big_brother.csv', 'SACRED EYE DATA', icon_size)
st_button('github', 'https://github.com/akshat-sj', 'Follow Akshat Singh Jaiswal on Github', icon_size)
st_button('github', 'https://github.com/VyoJ', 'Follow Vyoman Jain on Github', icon_size)
st_button('github', 'https://github.com/Divyanshu-Agrawal-526', 'Follow Divyanshu Agrawal on Github', icon_size)
st_button('github', 'https://github.com/N4SK4R', 'Follow Aditya Naskar on Github', icon_size)
st_button('github', 'https://github.com/akshat-sj/big-brother', 'Follow BIG BROTHER SOURCE CODE on Github', icon_size)
st_button('cup', 'https://www.buymeacoffee.com/dataprofessor/', 'Buy me a Coffee', icon_size)
@st.experimental_singleton
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from mytable;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
