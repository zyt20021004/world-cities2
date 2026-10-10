import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# TODO: 把 Siqi Zhou 换成你自己的名字（中英文都可以）
st.title("California Housing Data (1990) by Yuting Zhang")

housing = pd.read_csv("housing.csv")
locations = housing["ocean_proximity"].unique()

# main area: filter by median house value
value_filter = st.slider("Minimal Median House Value", 0, 500001, 200000)
df = housing[housing["median_house_value"] >= value_filter]

st.subheader("See more filters in the sidebar:")

# sidebar: filter by location type (all selected by default)
location_filter = st.sidebar.multiselect(
    "Choose the location type",
    locations,
    locations,
)
df = df[df["ocean_proximity"].isin(location_filter)]

# sidebar: filter by income level
income_filter = st.sidebar.radio(
    "Choose income level",
    ("Low", "Medium", "High"),
)

if income_filter == "Low":
    df = df[df["median_income"] <= 2.5]
elif income_filter == "Medium":
    df = df[(df["median_income"] > 2.5) & (df["median_income"] < 4.5)]
else:
    df = df[df["median_income"] >= 4.5]

# map of the filtered districts
st.map(df)

# histogram of median house value, 30 bins
st.subheader("Median House Value of the Filtered Districts")
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(df["median_house_value"], bins=30)
ax.set_xlabel("Median House Value (USD)")
ax.set_ylabel("Number of districts")
st.pyplot(fig)
