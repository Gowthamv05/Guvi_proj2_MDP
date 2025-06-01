import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Function to load models
def load_model(model_path):
    with open(model_path, 'rb') as file:
        return pickle.load(file)

# Load models
Kidney_model = load_model("model_kidney.pkl")
liver_model = load_model("model_Liver.pkl')
parkinson_model = load_model("model_parkinson.pkl')

# App title
st.title('Medical Condition Prediction App 🩺🏥')

# Sidebar for selecting conditions
condition = st.sidebar.selectbox('Select Medical Condition', ['Kidney Disease', 'Liver Disease', 'Parkinson Disease'])

# Function to display funny results
def display_funny_result(condition_name, prediction, advice):
    if prediction == 1:
        st.error(f"Oops! {condition_name} detected. 😅")
        st.write(f"💡 **Advice**: {advice}")
        st.write("🤣 **Fun Note**: Looks like your organs are staging a rebellion! Time to call in the health reinforcements!")
    else:
        st.success(f"No signs of {condition_name}. 🎉")
        st.write(f"💡 **Advice**: Keep doing what you're doing—your {condition_name.lower()} is in great shape!")
        st.write("🤣 **Fun Note**: Your organs are happy campers. Maybe treat them to a veggie smoothie?")

# Liver Disease Prediction
if condition == 'Liver Disease':
    st.header('Liver Disease Prediction 🥩')
    
    # Input fields
    Age = st.number_input('Age', min_value=1)
    Gender_select = st.selectbox('Gender', ['Male', 'Female'])
    Gender_map = {'Male': 1, 'Female': 0}
    Gender = Gender_map.get(Gender_select)
    Total_Bilirubin = st.number_input('Total_Bilirubin', min_value=0.0)
    Direct_Bilirubin = st.number_input('Direct_Bilirubin', min_value=0.0)
    Alkaline_Phosphotase = st.number_input('Alkaline_Phosphotase', min_value=0)
    Alamine_Aminotransferase = st.number_input('Alamine_Aminotransferase', min_value=0)
    Aspartate_Aminotransferase = st.number_input('Aspartate_Aminotransferase', min_value=0)
    Total_Protiens = st.number_input('Total_Protiens', min_value=0.0)
    Albumin = st.number_input('Albumin', min_value=0.0)
    Albumin_and_Globulin_Ratio = st.number_input('Albumin_and_Globulin_Ratio', min_value=0.0)
    
    # Prediction button
    if st.button('Predict Liver Disease'):
        data = {
            "Age": Age, "Gender": Gender, "Total_Bilirubin": Total_Bilirubin,
            "Direct_Bilirubin": Direct_Bilirubin, "Alkaline_Phosphotase": Alkaline_Phosphotase,
            "Alamine_Aminotransferase": Alamine_Aminotransferase,
            "Aspartate_Aminotransferase": Aspartate_Aminotransferase, "Total_Protiens": Total_Protiens,
            "Albumin": Albumin, "Albumin_and_Globulin_Ratio": Albumin_and_Globulin_Ratio
        }
        input_data = pd.DataFrame([data])
        prediction = liver_model.predict(input_data)
        advice = "Cut back on alcohol, avoid processed foods, and hydrate well!"
        display_funny_result("Liver Disease", prediction[0], advice)

# Kidney Disease Prediction
elif condition == 'Kidney Disease':
    st.header('Kidney Disease Prediction 🫘')

    # Input fields
    age = st.number_input('Age', min_value=1, max_value=120)
    bp = st.number_input('Blood Pressure (bp)', min_value=0.0)
    sg = st.number_input('Specific Gravity (sg)', min_value=1.000, max_value=1.050, step=0.001, format="%.3f")
    al = st.number_input('Albumin (al)', min_value=0)
    su = st.number_input('Sugar (su)', min_value=0)
    rbc = st.selectbox('Red Blood Cells (rbc)', ['Normal', 'Abnormal'])
    pc = st.selectbox('Pus Cell (pc)', ['Normal', 'Abnormal'])
    pcc = st.selectbox('Pus Cell Clumps (pcc)', ['Present', 'Not Present'])
    ba = st.selectbox('Bacteria (ba)', ['Present', 'Not Present'])
    bgr = st.number_input('Blood Glucose Random (bgr)', min_value=0.0)
    bu = st.number_input('Blood Urea (bu)', min_value=0.0)
    sc = st.number_input('Serum Creatinine (sc)', min_value=0.0)
    sod = st.number_input('Sodium (sod)', min_value=0.0)
    pot = st.number_input('Potassium (pot)', min_value=0.0)
    hemo = st.number_input('Hemoglobin (hemo)', min_value=0.0)
    pcv = st.number_input('Packed Cell Volume (pcv)', min_value=0)
    wc = st.number_input('White Blood Cell Count (wc)', min_value=0)
    rc = st.number_input('Red Blood Cell Count (rc)', min_value=0.0)
    htn = st.selectbox('Hypertension (htn)', ['Yes', 'No'])
    dm = st.selectbox('Diabetes Mellitus (dm)', ['Yes', 'No'])
    cad = st.selectbox('Coronary Artery Disease (cad)', ['Yes', 'No'])
    appet = st.selectbox('Appetite (appet)', ['Good', 'Poor'])
    pe = st.selectbox('Pedal Edema (pe)', ['Yes', 'No'])
    ane = st.selectbox('Anemia (ane)', ['Yes', 'No'])

    # Encoding inputs
    rbc_encoded = 1 if rbc == "Normal" else 0
    pc_encoded = 1 if pc == "Normal" else 0
    pcc_encoded = 1 if pcc == "Present" else 0
    ba_encoded = 1 if ba == "Present" else 0
    htn_encoded = 1 if htn == "Yes" else 0
    dm_encoded = 1 if dm == "Yes" else 0
    cad_encoded = 1 if cad == "Yes" else 0
    appet_encoded = 1 if appet == "Good" else 0
    pe_encoded = 1 if pe == "Yes" else 0
    ane_encoded = 1 if ane == "Yes" else 0

    input_data = np.array([
        age, rbc_encoded, pc_encoded, pcc_encoded, ba_encoded, htn_encoded,
        dm_encoded, cad_encoded, appet_encoded, pe_encoded, ane_encoded,
        bp, sg, al, su, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc
    ]).reshape(1, -1)

    # Prediction button
    if st.button("Predict Kidney Disease"):
        try:
            prediction = Kidney_model.predict(input_data)
            advice = "Stay hydrated, reduce salt intake, and monitor your blood pressure regularly."
            display_funny_result("Kidney Disease", prediction[0], advice)
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

# Parkinson Disease Prediction
elif condition == 'Parkinson Disease':
    st.header('Parkinson Disease Prediction 🧠')

    # Input fields
    MDVP_Fo_Hz = st.number_input('MDVP:Fo(Hz)', min_value=0.0)
    MDVP_Fhi_Hz = st.number_input('MDVP:Fhi(Hz)', min_value=0.0)
    MDVP_Flo_Hz = st.number_input('MDVP:Flo(Hz)', min_value=0.0)
    MDVP_Jitter_percent = st.number_input('MDVP:Jitter(%)', min_value=0.0)
    MDVP_Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', min_value=0.0)
    MDVP_RAP = st.number_input('MDVP:RAP', min_value=0.0)
    MDVP_PPQ = st.number_input('MDVP:PPQ', min_value=0.0)
    Jitter_DDP = st.number_input('Jitter:DDP', min_value=0.0)
    MDVP_Shimmer = st.number_input('MDVP:Shimmer', min_value=0.0)
    MDVP_Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', min_value=0.0)
    Shimmer_APQ3 = st.number_input('Shimmer:APQ3', min_value=0.0)
    Shimmer_APQ5 = st.number_input('Shimmer:APQ5', min_value=0.0)
    MDVP_APQ = st.number_input('MDVP:APQ', min_value=0.0)
    Shimmer_DDA = st.number_input('Shimmer:DDA', min_value=0.0)
    NHR = st.number_input('NHR', min_value=0.0)
    HNR = st.number_input('HNR', min_value=0.0)
    RPDE = st.number_input('RPDE', min_value=0.0)
    DFA = st.number_input('DFA', min_value=0.0)
    spread1 = st.number_input('spread1', min_value=-100.0, max_value=100.0)
    spread2 = st.number_input('spread2', min_value=0.0)
    D2 = st.number_input('D2', min_value=0.0)
    PPE = st.number_input('PPE', min_value=0.0)

    # Prediction button
    if st.button('Predict Parkinson Disease'):
        input_data = pd.DataFrame([{
            'MDVP:Fo(Hz)': MDVP_Fo_Hz, 'MDVP:Fhi(Hz)': MDVP_Fhi_Hz,
            'MDVP:Flo(Hz)': MDVP_Flo_Hz, 'MDVP:Jitter(%)': MDVP_Jitter_percent,
            'MDVP:Jitter(Abs)': MDVP_Jitter_Abs, 'MDVP:RAP': MDVP_RAP,
            'MDVP:PPQ': MDVP_PPQ, 'Jitter:DDP': Jitter_DDP, 'MDVP:Shimmer': MDVP_Shimmer,
            'MDVP:Shimmer(dB)': MDVP_Shimmer_dB, 'Shimmer:APQ3': Shimmer_APQ3,
            'Shimmer:APQ5': Shimmer_APQ5, 'MDVP:APQ': MDVP_APQ, 'Shimmer:DDA': Shimmer_DDA,
            'NHR': NHR, 'HNR': HNR, 'RPDE': RPDE, 'DFA': DFA, 'spread1': spread1,
            'spread2': spread2, 'D2': D2, 'PPE': PPE
        }])
        prediction = parkinson_model.predict(input_data)
        advice = "Exercise regularly, eat healthy, and consult a neurologist for expert guidance."
        display_funny_result("Parkinson Disease", prediction[0], advice)
