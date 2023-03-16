import streamlit
import pandas as pd
streamlit.title("My Parents New Healthy Diet")
streamlit.header(" BreakFast Menu")
streamlit.text("🥣 Omega 3 & Blueberry oat meal")
streamlit.text("🥗 Kale, Spinach")
streamlit.text("🐔 Hard-boiled")
streamlit.text("🥑🍞 Avacdo")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruits_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruits_list = my_fruits_list.set_index("Fruit")
streamlit.multiselect("Pick some fruits",list(my_fruits_list.index),['Avocado','Strawberries'])
streamlit.dataframe(my_fruits_list)
