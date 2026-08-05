# 📊 prediction_app.py

import streamlit as st
import pandas as pd
import joblib

# Load trained model

model = joblib.load('models/attendance_model.pkl')

st.title("🎓 Smart Attendance Prediction System")

st.write("Enter student details to predict attendance percentage")

# User Inputs

study_hours = st.slider("Study Hours per Day", 0, 10, 5)
sleep_hours = st.slider("Sleep Hours per Day", 0, 10, 7)
participation = st.selectbox("Class Participation", ["Low", "Medium", "High"])
previous_grade = st.slider("Previous Grade (%)", 0, 100, 70)
internet_usage = st.slider("Internet Usage (hrs/day)", 0, 10, 4)
health = st.selectbox("Health Condition", ["Poor", "Average", "Good"])

# Convert categorical to numerical (same as training)

input_data = pd.DataFrame({
'Study_Hours': [study_hours],
'Sleep_Hours': [sleep_hours],
'Previous_Grade': [previous_grade],
'Internet_Usage': [internet_usage],

```
# One-hot encoding manually
'Participation_Low': [1 if participation == "Low" else 0],
'Participation_Medium': [1 if participation == "Medium" else 0],
'Participation_High': [1 if participation == "High" else 0],

'Health_Condition_Poor': [1 if health == "Poor" else 0],
'Health_Condition_Average': [1 if health == "Average" else 0],
'Health_Condition_Good': [1 if health == "Good" else 0]
```

})

# Prediction

if st.button("Predict Attendance"):
prediction = model.predict(input_data)[0]
st.success(f"📈 Predicted Attendance: {prediction:.2f}%")
