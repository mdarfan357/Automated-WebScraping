import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import seaborn as sns

os.chdir("../price_track")
st.write("Price Tracker")
data = pd.read_csv("price_track.csv")
st.write(data)
st.line_chart(data.remove(columns=["date"])) 
st.button("Refresh")
