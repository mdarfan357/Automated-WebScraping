import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import seaborn as sns

os.chdir("../price_track")
st.write("Price Tracker")
data = pd.read_csv("price_track.csv")
data2 = data.drop(columns = ["Date"])
data1 = data.pop("Date")
st.write(data1)
st.write(data2)
st.line_chart(data2)
st.button("Refresh")
