import streamlit as st 


st.title("월간 논문")

with st.form("select_month"):
   years = [ 2023,3034]
   months = [ 1,2,3,4,5,6,7,8,9,10,11,12]
   st.write("조회하고 싶은 논문의 년도와 월을 선택하세요")
   col1, col2, col3 = st.columns(3) 
   with col1: 
       selected_year = st.selectbox("Year", options = years)
   with col2: 
       selected_month = st.selectbox("Month", options =  months )
   # Every form must have a submit button.
   with col3: 
      submitted = st.form_submit_button("Submit")

   if submitted:
       st.write(selected_year,'년',  selected_month, "월" )

st.write("Outside the form")