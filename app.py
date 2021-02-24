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

st.title("Hello World!")

Map = folium.Map()
folium_static(Map)

