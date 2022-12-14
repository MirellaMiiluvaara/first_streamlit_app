import streamlit
streamlit.title('My Mom´s new healthy diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Blueberry porrige')
streamlit.text('🥗 Smoothie')
streamlit.text('🐔 Omelet')
streamlit.text('🥑🍞 Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Adding multiselect list
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

#Display table
streamlit.dataframe(my_fruit_list)
