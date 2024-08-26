import streamlit as st
st.title("CO2 Prediction")
import numpy as np
import pickle
with open ("ff.pkl",'rb') as file:
    co2_model= pickle.load(file)
def prediction(Engine_Size, Cylinders, Fuel_Consumption1,Fuel_Consumption2,Fuel_Consumption3,Smog_Level):
    data= np.array([[Engine_Size, Cylinders, Fuel_Consumption1,Fuel_Consumption2,Fuel_Consumption3,Smog_Level]])
    final_model= co2_model.predict(data)
    return final_model
Engine_Size= st.slider("Engine_Size",min_value=1,max_value=30)
Cylinders= st.slider("Cylinders",min_value=.5,max_value=100.4)
Fuel_Consumption1= st.slider("Fuel_Consumption1",min_value=.5,max_value=100.4)
Fuel_Consumption2= st.slider("Fuel_Consumption2",min_value=.5,max_value=100.4)
Fuel_Consumption3= st.slider("Fuel_Consumption3",min_value=.5,max_value=100.4)
Smog_Level= st.slider("Smog_Level",min_value=.5,max_value=100.4)
if st.button("Predict"):
    st.write(f"The prediction value{Engine_Size}, {Cylinders}, {Fuel_Consumption1},{Fuel_Consumption2},{Fuel_Consumption3},{Smog_Level}")
    final_value= prediction(Engine_Size, Cylinders, Fuel_Consumption1,Fuel_Consumption2,Fuel_Consumption3,Smog_Level)
    st.write({final_value[0]})
    



