import streamlit as st
from send_email import send_mail


st.header("Contact Me")

with st.form(key="email_form"): #to create form, key is required in st.form
    user_email = st.text_input("Enter your email") #to input email
    raw_message = st.text_area("Your message") #to create big text area
    message = f"""
Subject: New email from {user_email}\n
From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit") #this is special button for submit belonged form
    if button:
        send_mail(message)
        st.info("Email was sent")
