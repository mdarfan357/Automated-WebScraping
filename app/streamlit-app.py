import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

path = "mdarfan357/price_track/edit/main/app"

os.chdir("../price_track")
st.write("Price Tracker")
# st.write(os. getcwd())
data = pd.read_csv("price_track.csv")
st.write(data)
st.button("Refresh")
