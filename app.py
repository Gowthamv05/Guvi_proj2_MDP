import streamlit as st
import numpy as np
import pandas as pd
import pickle

def load_model(model_path):
    with open(model_path, 'rb') as file:
        return pickle.load(file)


Kidney_model=load_model(r"C:\Users\sisir\.streamlit\eenv\Scripts\model_kidney.pkl")
liver_model = load_model(r'C:\Users\sisir\.streamlit\eenv\Scripts\model_Liver.pkl')
parkinson_model = load_model(r'C:\Users\sisir\.streamlit\eenv\Scripts\model_parkinson.pkl')


st.title('Medical Condition Prediction App')
st.sidebar.write('Select parameters and click Predict to see the results.')




condition = st.sidebar.selectbox('Select Medical Condition', ['Kidney Disease','Liver Disease', 'Parkinson Disease'])

if condition == 'Liver Disease':
    st.header('Liver Disease Prediction')
    
   
    age = st.number_input('Age', min_value=1)
    gender_select = st.selectbox('Gender', ['Male', 'Female'])
    gender_map={'Male':1, 'Female':0}
    gender=gender_map.get(gender_select)
    bilirubin = st.number_input('Total Bilirubin',min_value=0)
    Direct_Bilirubin=st.number_input('Direct_Bilirubin',min_value=0)
    alkaline_phosphotase = st.number_input('Alkaline Phosphotase',min_value=0)
    Alamine_Aminotransferase= st.number_input('Alamine_Aminotransferase',min_value=0)
    Aspartate_Aminotransferase=st.number_input('Aspartate_Aminotransferase',min_value=0)
    Total_Protiens=st.number_input('Total_Protiens',min_value=0)
    albumin = st.number_input('Albumin',min_value=0)
    Albumin_and_Globulin_Ratio=st.number_input('Albumin_and_Globulin_Ratio',min_value=0)
    
    if st.button('Predict'):
        data={
            "Age":age,"Gender":gender,"Total_Bilirubin":bilirubin,"Direct_Bilirubin":Direct_Bilirubin,
            "Alkaline_Phosphotase":alkaline_phosphotase,"Alamine_Aminotransferase":Alamine_Aminotransferase,
            "Aspartate_Aminotransferase":Aspartate_Aminotransferase,"Total_Protiens":Total_Protiens,
            "Albumin":albumin,"Albumin_and_Globulin_Ratio":Albumin_and_Globulin_Ratio
            }
        input_data = pd.DataFrame([data])
        prediction = liver_model.predict(input_data)
        st.write('Prediction:', 'Positive' if prediction[0] == 1 else 'Negative')
