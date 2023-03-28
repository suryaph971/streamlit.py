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


def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
  

try:
  fruit_choice = streamlit.text_input('What do you want to know about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
  #streamlit.text(fruityvice_response.json())


    
    
except URLError as e:
  streamlit.error()


streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
  my_cur = my_con.cursor()
  my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
  my_data_row = my_cur.fetchall()
  return my_data_row

if streamlit.button('Get Fruit Load List'):
  my_con = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_con.close()
  streamlit.dataframe(my_data_rows)

def insert_row_snowflake(newfruit):
  my_cur = my_con.cursor()
  my_cur.execute("insert into fruit_load_list values ('from streamlit')")
  return "Thanks for adding " +newfruit
add_my_fruit = streamlit.text_input("What fruit would you like to add?")
if streamlit.button('Add a fruit'):
  my_con = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)
