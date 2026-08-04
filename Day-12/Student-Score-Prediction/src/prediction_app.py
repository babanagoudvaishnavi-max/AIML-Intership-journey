import pickle

# Load trained model
with open('models/student_model.pkl', 'rb') as f:
    model = pickle.load(f)

# User input
hours = float(input("Enter study hours: "))

# Prediction
prediction = model.predict([[hours]])

print(f"📊 Predicted Score: {prediction[0]:.2f}")
