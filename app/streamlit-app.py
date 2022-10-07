import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import seaborn as sns
import altair as alt

os.chdir("../price_track")
st.write("Price Tracker")
data = pd.read_csv("price_track.csv")
data1 = data.drop(columns = ["Date"])
st.write(data)
# st.line_chart(data1)
# st.button("Refresh")

chart = alt.Chart(data).mark_circle().encode(x='a',y='b',size='c',color='c',tooltip=['a','b'])

st.altair_chart(chart, use_container_width=True)

st.subheader("This is a line chart")
st.line_chart(data1)  
st.subheader("This is a area chart")
st.area_chart(data1)
st.subheader("This is a bar chart")
st.bar_chart(data1)
st.subheader("This is a matplotlib chart")
