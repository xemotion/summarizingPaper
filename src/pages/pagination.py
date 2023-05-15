import streamlit as st 
import pandas as pd 

pagination = st.container()
FILEPATH = "D:/workspace/streamlist_prj/src/data/block_chain.csv"


df = pd.read_csv(FILEPATH) 

bottom_menu = st.columns((4, 1, 1))
with bottom_menu[2]:
    batch_size = st.selectbox("Page Size", options=[25, 50, 100])
with bottom_menu[1]:
    total_pages = (
        int(len(df) / batch_size) if int(len(df) / batch_size) > 0 else 1
    )
    current_page = st.number_input(
        "Page", min_value=1, max_value=total_pages, step=1
        st.dataframe()
    )
with bottom_menu[0]:
    st.markdown(f"Page **{current_page}** of **{total_pages}** ")