import streamlit as st
import streamlit.components.v1 as components  # use 'components', not 'component'

st.title("Control A website!")

# Create an entry box
url1 = st.text_input("Enter URL:")

if st.button("Start Web"):
    iframe_code = f'<iframe src="{url1}" width="800" height="600" frameborder="0"></iframe>'
    components.html(iframe_code, height=600, scrolling=True)  # <- now correct
