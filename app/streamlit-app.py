import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import seaborn as sns

os.chdir("../price_track")
# st.write("## ")
st. markdown("<h1 style='text-align: center; color: white;'>Price Tracker</h1>", unsafe_allow_html=True)
st.write("Here we use data collected from websites to display trends in product prices.")
st.write("These help people take better descion about the product they wanna buy and the time at which they want to buy the product")

st.write("#### Dataset :")
data = pd.read_csv("price_track.csv")
data1 = data.drop(columns = ["Date"])
st.write(data)
# st.line_chart(data1)
# st.button("Refresh")


# st.subheader("")
st. markdown("<h3 style='text-align: center; color: white;'>This is a line chart</h3>", unsafe_allow_html=True)
st.line_chart(data1)  
st. markdown("<h3 style='text-align: center; color: white;'>This is a area chart</h3>", unsafe_allow_html=True)
st.area_chart(data1)
st. markdown("<h3 style='text-align: center; color: white;'>This is a bar chart</h3>", unsafe_allow_html=True)
st.bar_chart(data1)

