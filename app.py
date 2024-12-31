import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('predictor.pickle', 'rb') as file:
    model = pickle.load(file)

# Page Title
st.title("Laptop Price Predictor 💻")
st.write("Enter the laptop specifications to predict the price.")

# Input Fields
ram = st.selectbox("RAM (GB):", [4, 8, 16, 32, 64])
weight = st.number_input("Weight (kg):", min_value=0.5, max_value=5.0, value=1.5, step=0.1)
touchscreen = st.selectbox("Touchscreen:", ["No", "Yes"])
ips = st.selectbox("IPS Display:", ["No", "Yes"])

# Categorical Inputs (Company, TypeName, OS, CPU, GPU)
company = st.selectbox("Company:", ['Acer', 'Apple', 'Asus', 'Dell', 'HP', 'Lenovo', 'MSI', 'Other', 'Toshiba'])
type_name = st.selectbox("Type Name:", ['Gaming', 'Netbook', 'Notebook', 'Ultrabook', 'Workstation'])
os = st.selectbox("Operating System:", ['Linux', 'Mac', 'Other', 'Windows'])
cpu_name = st.selectbox("CPU Name:", ['AMD', 'Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'Other'])
gpu_name = st.selectbox("GPU Name:", ['AMD', 'Intel', 'Nvidia'])

# Feature Encoding
# Binary encoding for Touchscreen and IPS
touchscreen_binary = 1 if touchscreen == "Yes" else 0
ips_binary = 1 if ips == "Yes" else 0

# One-Hot Encoding for Categorical Features
company_encoding = ['Acer', 'Apple', 'Asus', 'Dell', 'HP', 'Lenovo', 'MSI', 'Other', 'Toshiba']
type_encoding = ['2 in 1 Convertible', 'Gaming', 'Netbook', 'Notebook', 'Ultrabook', 'Workstation']
os_encoding = ['Linux', 'Mac', 'Other', 'Windows']
cpu_encoding = ['AMD', 'Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'Other']
gpu_encoding = ['AMD', 'Intel', 'Nvidia']

# Encode selected values
input_features = [
    ram, 
    weight, 
    touchscreen_binary, 
    ips_binary
]

# Company Encoding
for c in company_encoding:
    input_features.append(1 if company == c else 0)

# Type Encoding
for t in type_encoding:
    input_features.append(1 if type_name == t else 0)

# OS Encoding
for o in os_encoding:
    input_features.append(1 if os == o else 0)

# CPU Encoding
for c in cpu_encoding:
    input_features.append(1 if cpu_name == c else 0)

# GPU Encoding
for g in gpu_encoding:
    input_features.append(1 if gpu_name == g else 0)

# Prediction
if st.button("Predict Price"):
    # Reshape input as model expects a 2D array
    input_array = np.array(input_features).reshape(1, -1)
    predicted_price = model.predict(input_array)
    st.success(f"Predicted Laptop Price: RS {predicted_price[0]:.2f}")
