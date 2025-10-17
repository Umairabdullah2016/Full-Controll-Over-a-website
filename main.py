import streamlit as st
import streamlit.components.v1 as component

st.title("Control A website!")

# Create an entry box
url = st.text_input("Enter url: ")



if st.button("Start Web"):
    iframe_code = f'<iframe src="{url}" width="800" height="600" frameborder="0"></iframe>'
    component.html(iframe_code, height=600, scrolling=True)
