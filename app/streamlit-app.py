import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import seaborn as sns

os.chdir("../price_track")

st.markdown("<h1 style='text-align: center;'>Price Tracker</h1>", unsafe_allow_html=True)
st.image("https://editor.analyticsvidhya.com/uploads/80484Thumbnail.png")
st.write("Here we use data collected from websites to display trends in product prices.")
st.write("These help people take better descion about the product they wanna buy and the time at which they want to buy the product")

st.write("#### Dataset :")
data = pd.read_csv("price_track.csv")
data1 = data.drop(columns = ["Date"])
st.write(data)
# st.line_chart(data1)
# st.button("Refresh")


# st.subheader("")
st.markdown("<h3 style='text-align: center;'>This is a line chart</h3>", unsafe_allow_html=True)
st.line_chart(data1)  
st.markdown("<h3 style='text-align: center;'>This is a area chart</h3>", unsafe_allow_html=True)
st.area_chart(data1)
st.markdown("<h3 style='text-align: center;'>This is a bar chart</h3>", unsafe_allow_html=True)
st.bar_chart(data1)

st.write()
latest_amz = int(data1[-1:]["Amazon price"])
latest_flip = int(data1[-1:]["Flipkart price"])

if latest_amz > latest_flip:
  st.markdown("<p style='text-align: center;'>Amazon has the least price for the following product.</p>", unsafe_allow_html=True)
if latest_amz > latest_flip:
  st.markdown("<p style='text-align: center;'>Flipkart has the lowest price for the following product.</p>", unsafe_allow_html=True)
else:
  st.markdown("<p style='text-align: center;'>Both websites have the same price for the following product.</p>", unsafe_allow_html=True)
st.write("To know more about the next sale check out this [link](https://www.newindianexpress.com/expressdeals/other-categories/amazon-upcoming-sale-in-india/218.html)")
st.write("Also keep in touch with the official websites [Amazon](https://www.amazon.in/), [Flipkart](https://www.flipkart.com/)")

st.write("----------------------------------------------------")


# st.markdown("<img style='text-align: center;'>https://media0.giphy.com/media/R6gvnAxj2ISzJdbA63/giphy.gif?cid=511e7ad3cmz597iamlotymrf0egpx8ew3xkz592tbj9r40d0&rid=giphy.gif&ct=g</img>", unsafe_allow_html=True)


_left, mid, _right = st.columns(3)
with mid:
   st.image("https://media0.giphy.com/media/R6gvnAxj2ISzJdbA63/giphy.gif?cid=511e7ad3cmz597iamlotymrf0egpx8ew3xkz592tbj9r40d0&rid=giphy.gif&ct=g",width=400)


st.markdown("<p style='text-align: center;'>Please leave a like if you liked the website and share it with your friends.</p>", unsafe_allow_html=True)
_left2, mid2, _right2 = st.columns(3)
with mid2:
      but = st.button("Like")
      if but:
         st.balloons()
         st.write("Appreciate it :)")
        



 
