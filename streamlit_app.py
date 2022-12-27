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
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Display table
streamlit.dataframe(fruits_to_show)

#New section to display fruityvice response
streamlit.header('Fruityvice fruit advice')

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#streamlit.text(fruityvice_response.json())

#Normalize response
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#Display normalized result
streamlit.dataframe(fruityvice_normalized)

