import streamlit as st 
import joblib 

#load the joblib model 
model_nb = joblib.load('Cars.csv')

#user input 
st.title("Cars body-style")
ip = st.text_input("Enter your message:")

             
           

  
                                    
  
