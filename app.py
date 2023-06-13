import streamlit as st

st.title("Hello World!")
if st.button('run'):
    for i in range(10):
        st.subheader(i)
st.subheader("hello!")
st.header("Hello!")
st.title("Hello!")
st.markdown("## Hello!")
