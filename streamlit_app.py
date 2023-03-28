import streamlit
import pandas as pd
import snowflake.connector
from urllib.error import URLError
streamlit.title("My Parents New Healthy Diet")
streamlit.header(" BreakFast Menu")
streamlit.text("🥣 Omega 3 & Blueberry oat meal")
streamlit.text("🥗 Kale, Spinach")
streamlit.text("🐔 Hard-boiled")
streamlit.text("🥑🍞 Avacdo")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruits_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruits_list = my_fruits_list.set_index("Fruit")
fruits_selected = streamlit.multiselect("Pick some fruits",list(my_fruits_list.index),['Avocado','Strawberries'])
streamlit.dataframe(my_fruits_list.loc[fruits_selected])

streamlit.header("Fruityvice Fruit Advice!")
import requests
fruit_choice = streamlit.text_input('What do you want to know about?','kiwi')
streamlit.write('The user entered',fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#streamlit.text(fruityvice_response.json())


fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)


streamlit.stop()
my_con = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_con.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)
add_my_fruit = streamlit.text_input("What fruit would you like to add?","jackfruit")
streamlit.write("Thanks for adding",add_my_fruit)
my_cur.execute("insert into fruit_load_list values('from streamlit')")
