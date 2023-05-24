import streamlit as st

st.set_page_config(layout="wide")  #this is how we write configuration of our webpage

col1, col2 = st.columns(2) #method

with col1:
    st.image("/Users/savchik/Desktop/python/2app/images/photo.png", width = "300") #image - method which produces image object

with col2: 
    st.title("Sava Sevs")
    content = """""
    Hi , i am Sava Sevs! I am creating rpogram code with Python. I just doing my second Python course and ready for new knowledge. Let's see what we got!
    """""
    st.info(content) #we used st.info instead of st.write and it changed appearance of content and made it with blue font