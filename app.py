## _*_ coding:utf-8 _*_
#************************************************#
# File Name: app.py
# Author: liupu
# mail: lpgauss@163.com
# Created Time: 三  2/24 21:33:28 2021
#************************************************#

import numpy as np 
import pandas as pd 
import streamlit as st 
import folium 
from streamlit_folium import folium_static

name = st.sidebar.textinput("Please enter your name")

press = st.sidebar.button("Press")

st.title("Hello World!")
if press:
    Map = folium.Map(location=[28.234562,112.324532],zoom_start=12)
    folium_static(Map)

X = np.random.randn(100)
y = X * 10 + np.random.randn()

Data = pd.DataFrame({"X":X,"Y":y})

st.write("Table show")
st.write(Data)

