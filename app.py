import streamlit as st 
import joblib 

#load the joblib model 
model_nb = joblib.load('news_category')

#user input 
st.title("NEWS CATEGORY")
ip = st.text_input("Enter your message:")
 
op = model_nb.predict([ip])
if st.button('Predict Category'):
  st.title(op[0])  

             
           

  
                                    
  
