import streamlit as st 
import joblib 

#load the joblib model 
model_nb = joblib.load('Cars.csv')

#user input 
st.title("Cars body-style")
ip = st.text_input("Enter your message:")

#predict if the entered message belongs to sports,world,politics 
op = model_nb.predict([ip])
if st.button('Predict style'):
  st.title(op[0])  #prints the output as  sports or politics or world
             
           

  
                                    
  
