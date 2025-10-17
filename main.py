import streamlit as st

st.title("Control A website!")

# Create an entry box
urk = st.text_input("Enter url: ")



if st.button("Start Web"):
    iframe_code = f'<iframe src="{url}" width="800" height="600" frameborder="0"></iframe>'
    components.html(iframe_code, height=600, scrolling=True)
