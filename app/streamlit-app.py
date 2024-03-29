import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

os.chdir("../automated-webscraping")

st.markdown("<h1 style='text-align: center;'>Price Tracker</h1>", unsafe_allow_html=True)
st.image("https://editor.analyticsvidhya.com/uploads/80484Thumbnail.png")
st.write("Here we use data collected from websites to display trends in product prices.")
st.write("These help people take better decision about the product they wanna buy and the time at which they want to buy the product")
st.write('Please note that a "0" as the product price indicates that the product is not available at the moment')
st.write("#### Dataset :")
data = pd.read_csv("price_track.csv")

st.sidebar.subheader("Data size ")
data_size = st.sidebar.selectbox("How much data?",["6 Months","2 Months","1 Month","10 days"])

if data_size == "6 Months":
    data_size = 180
if data_size == "2 Months":
    data_size = 60
if data_size == "1 Month":
    data_size = 30
if data_size == "10 days":
    data_size = 10

st.dataframe(data.tail(data_size))

data1 = data.drop(columns = ["Date"])

st.markdown("<h3 style='text-align: center;'>Price of the desired product</h3>", unsafe_allow_html=True)
st.line_chart(data1.tail(data_size))  

latest_amz = int(data1[-1:]["Amazon price"])
latest_flip = int(data1[-1:]["Flipkart price"])
st.write(f"latest_flip: {latest_flip},latest_amz : {latest_amz}")


if latest_amz == latest_flip:
  st.markdown("<p style='text-align: center;'>Both websites have the same price for the following product.</p>", unsafe_allow_html=True)
elif latest_amz > latest_flip:
  st.markdown("<p style='text-align: center;'>Amazon has the least price for the following product.</p>", unsafe_allow_html=True)
elif latest_amz < latest_flip:
  st.markdown("<p style='text-align: center;'>Flipkart has the lowest price for the following product.</p>", unsafe_allow_html=True)

st.write("To know more about the next sale check out this [link](https://www.newindianexpress.com/expressdeals/other-categories/amazon-upcoming-sale-in-india/218.html)")
st.write("Also keep in touch with the official websites [Amazon](https://www.amazon.in/), [Flipkart](https://www.flipkart.com/)")

st.write("----------------------------------------------------")


# st.markdown("<img style='text-align: center;'>https://media0.giphy.com/media/R6gvnAxj2ISzJdbA63/giphy.gif?cid=511e7ad3cmz597iamlotymrf0egpx8ew3xkz592tbj9r40d0&rid=giphy.gif&ct=g</img>", unsafe_allow_html=True)


_left, mid, _right,r1,r2 = st.columns(5)
with mid:
   st.image("https://media0.giphy.com/media/R6gvnAxj2ISzJdbA63/giphy.gif?cid=511e7ad3cmz597iamlotymrf0egpx8ew3xkz592tbj9r40d0&rid=giphy.gif&ct=g",width=400)


st.write("Please leave a like if you liked the website and share it with your friends.")

l1,l2,mid,r1,r2,r3,r4,r5,r6,r7 = st.columns(10)
with r7:
   but = st.button("Like")
if but:
   st.balloons()
   st.write("Appreciate it :)")
  
  
        



 
