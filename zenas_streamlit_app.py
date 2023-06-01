import streamlit
import snowflake.connector
import pandas

streamlit.title('Zena\'s Amazing Athleisure Catalog')
my_Cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_Cnx.cursor()

my_cur.execute("select color_or_style from catalog_for_website")
my_catalog=my_cur.fetchall()


df=pandas.DataFrame(my_catalog)
colors_list=df[0].values.to_list()

option=streamlit.selectbox('Pick a sweatsuit color or style:',list(colors_list))

product_caption = 'Our warm, Comfortable, ' + option + 'sweatsuit!'

my_cur.execute("select direct_url,price,size_list,upsell_product_desc from catalog_for_website where color_or_style='" + option + "';")

df2=my_cur.fetchone()

streamlit.image(
  df2[0],
  width=400,
  caption=product_caption
)

streamlit.write('Price:',df2[1])
streamlit.write('Sizes Available:',df2[2])
streamlit.write(df2[3])
