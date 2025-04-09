# app.py
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model

st.title("💎 Diamond Price Predictor")

st.write("Enter diamond features to predict its price:")

try:
    carat = float(st.text_input('Carat', '1.0'))
    depth = float(st.text_input('Depth', '60.0'))
    table = float(st.text_input('Table', '57.0'))
    x = float(st.text_input('Length (x)', '5.0'))
    y = float(st.text_input('Width (y)', '5.0'))
    z = float(st.text_input('Height (z)', '3.0'))
except ValueError:
    st.error("Please enter valid numeric values for all fields.")


# Categorical inputs (example)
cut = st.selectbox('Cut', ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
color = st.selectbox('Color', ['D', 'E', 'F', 'G', 'H', 'I', 'J'])
clarity = st.selectbox('Clarity', ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])

# Encoding (you can use LabelEncoder mapping if that's how it was trained)
input_df = pd.DataFrame({
    'carat': [carat],
    'depth': [depth],
    'table': [table],
    'x': [x],
    'y': [y],
    'z': [z],
    'cut': [cut],
    'color': [color],
    'clarity': [clarity]
})

# Load model, label encoders, and scaler
@st.cache_resource
def load_model_and_preprocessors():
    with open('./model/model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('./model/label_encoders.pkl', 'rb') as f:
        label_encoders = pickle.load(f)
    with open('./model/scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    return model, label_encoders, scaler

model, label_encoders, scaler = load_model_and_preprocessors()

# Encode categorical features
for col in ['cut', 'color', 'clarity']:
    encoder = label_encoders[col]
    input_df[col] = encoder.transform(input_df[col])

# Scale numerical features
numerical_cols = ['carat', 'depth', 'table', 'x', 'y', 'z']
input_df[numerical_cols] = scaler.transform(input_df[numerical_cols])

correct_order = ['carat', 'cut', 'color', 'clarity','depth', 'table', 'x', 'y', 'z']

input_df = input_df[correct_order]
# Make prediction
if st.button("Predict Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Diamond Price: 💲{prediction:,.2f}")