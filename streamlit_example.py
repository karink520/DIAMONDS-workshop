import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datset
penguins_df = pd.read_csv("penguins.csv")

# Use streamlit to display some text
st.write("This is an example streamlit app using the Palmer penguins dataset from Allison Horst")
st.write("https://allisonhorst.github.io/palmerpenguins/")

# Set up the radio buttons in two columns
col1, col2 = st.columns(2)
with col1:
    x_var_name = st.radio("Choose first variable", penguins_df.columns)

with col2:
    y_var_name = st.radio("Choose second variable", penguins_df.columns)

# Make the plot
fig, ax = plt.subplots()
sns.scatterplot(x=x_var_name, y=y_var_name, data=penguins_df, hue="species", ax=ax)
ax.set_title("")

# Use streamlit to display the plot
st.pyplot(fig)
