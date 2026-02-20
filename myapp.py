import streamlit as st
import numpy as np
import pandas as pd

st.title("My Streamlit App :streamlit:")
st.write("This is a simple Streamlit app.")
st.text("You can add more features and functionalities as needed.")

name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.success(f"Hello {name}!")
    
df=pd.DataFrame(np.random.randn(10, 2), columns=['Column 1', 'Column 2'])
st.line_chart(df)
st.bar_chart(df)

st.sidebar.header("Sidebar")
st.image("Kailash.jpeg", caption="Kailash") 

upload_file = st.file_uploader("Upload a file", type="csv")
if upload_file:
    df=pd.read_csv(upload_file)
    st.dataframe(df)
    
st.title("text and markdown demo")
st.header("this is a header")
st.subheader("this is a subheader")
st.markdown("**Bold**,*Italic* ,`code`,[Link](https://www.google.com)")
st.code("for i in range(5):\n    print(i)", language="python")
st.text_input("what is your name?")
st.text_area("write something about yourself")
st.number_input("pick a number", min_value=0, max_value=100, )
st.slider("choose a range",0,100)
st.selectbox("select an fruit", ["apple", "mango", "banana"])
st.multiselect("select your hobbies", ["reading", "traveling", "cooking", "sports"])    
st.radio("select your choice:",["option 1", "option 2", "option 3"])
st.checkbox("I agree to the terms and conditions")

if(st.checkbox("show more")):
    st.write("Here is some more information...")
    
option=st.radio("Choose view",["show chart","show table"])
if option=="show chart":
    st.write("Here is the chart view")
else:    
    st.write("Here is the table view")
    
with st.form("login_form"):
    username=st.text_input("Username")
    password=st.text_input("Password", type="password")
    submitted=st.form_submit_button("Login")
    if submitted:
        st.success(f"Welcome {username}!")