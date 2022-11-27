import streamlit as st
from st_functions import st_button, load_css
from PIL import Image
import mysql.connector

load_css()

st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.jpeg'))

st.header('BIG BROTHER')
icon_size = 20
st.header(st_button('webcam','SACRED EYE',icon_size)
          


st.info('Developed by Akshat Singh Jaiswal, Vyoman Jain, Aditya Naskar and Divyanshu Agrawal')


st_button('github', 'https://github.com/akshat-sj', 'Follow Akshat Singh Jaiswal on Github', icon_size)
st_button('github', 'https://github.com/VyoJ', 'Follow Vyoman Jain on Github', icon_size)
st_button('github', 'https://github.com/Divyanshu-Agrawal-526', 'Follow Divyanshu Agrawal on Github', icon_size)
st_button('github', 'https://github.com/N4SK4R', 'Follow Aditya Naskar on Github', icon_size)
st_button('github', 'https://github.com/akshat-sj/big-brother', 'Follow BIG BROTHER SOURCE CODE on Github', icon_size)
