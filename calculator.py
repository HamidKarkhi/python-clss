# pip install streamlit-
# run : python -m streamlit run calculator.py
import streamlit as st 

st.title("Welcom to my Calculator")
st.markdown("Performs all the operation easily") 

c1,c2=st.columns(2)
fnum = c1.number_input("Enter fist number",value=0)        #fnum mtalb [fist number]
snum = c2.number_input("Enter secound",value=0)            #snum mins [second number]

operations = ["Add","sub","Mul","Div"]
choice = st.radio("select an peration",operations)          

button = st.button("Calculate")

result = 0
if button:
    if choice=="Add":
        result = fnum+snum
    if choice=="sub":
        result = fnum-snum
    if choice=="Mul":
        result = fnum*snum
    if choice=="Div":
        result = fnum/snum
st.success(f"Result is {result}")
 
st.balloons
st.snow


