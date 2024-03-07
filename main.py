import streamlit as st
st.title('Login Form')

email = st.text_input('Enter Email')
password = st.text_input('Enter Password', type='password')


credentials = {'FS23AI009': 'aaryan', 'FS23AI003': 'rashid', 'FS23AI010': 'rohit'}
btn = st.button('Login')


if btn:
    if email in credentials and credentials[email] == password:
        st.snow()
    else:
        st.error('Login Failed! Incorrect Email or Password.')



