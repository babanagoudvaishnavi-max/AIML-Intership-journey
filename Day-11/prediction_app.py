# Day 11 – Prediction App

import numpy as np
import joblib
from sklearn.linear_model import LinearRegression

# Step 1: Train & Save Model (Run only once)
def train_and_save_model():
    hours = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
    scores = np.array([35, 40, 50, 55, 65, 70, 80, 90])

    model = LinearRegression()
    model.fit(hours, scores)

    joblib.dump(model, "student_model.pkl")
    print("Model trained and saved!")

# Step 2: Load Model
def load_model():
    return joblib.load("student_model.pkl")

# Step 3: Prediction App
def predict_score():
    model = load_model()

    hours = float(input("Enter study hours: "))
    prediction = model.predict([[hours]])

    print(f"Predicted Score: {prediction[0]:.2f}")

# Run program
if __name__ == "__main__":
  predict_score()
