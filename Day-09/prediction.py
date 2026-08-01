# Day 9 – Prediction Project (Complete Version)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import joblib


def train_model():
    """Train Linear Regression model and return it"""
    hours = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
    scores = np.array([35, 40, 50, 55, 65, 70, 80, 90])

    model = LinearRegression()
    model.fit(hours, scores)

    return model, hours, scores


def save_model(model):
    """Save model to file"""
    joblib.dump(model, "student_model.pkl")
    print("💾 Model saved as student_model.pkl")


def load_model():
    """Load model from file"""
    return joblib.load("student_model.pkl")


def evaluate_model(model, hours, scores):
    """Evaluate model performance"""
    predictions = model.predict(hours)
    accuracy = r2_score(scores, predictions)

    print(f"📊 Model Accuracy (R² Score): {accuracy:.2f}")
    return predictions


def predict_scores(model):
    """Take user input and predict scores"""
    while True:
        user_input = input("\nEnter study hours (comma separated) or 'exit': ")

        if user_input.lower() == "exit":
            print("👋 Exiting program...")
            break

        try:
            input_hours = list(map(float, user_input.split(",")))

            if any(h < 0 for h in input_hours):
                print("⚠️ Please enter positive values only.")
                continue

            input_array = np.array(input_hours).reshape(-1, 1)
            predicted_scores = model.predict(input_array)

            for h, s in zip(input_hours, predicted_scores):
                print(f"📘 Study Hours: {h} → 🎯 Predicted Score: {s:.2f}")

        except ValueError:
            print("⚠️ Invalid input! Please enter numbers correctly.")


def plot_graph(hours, scores, predictions):
    """Plot actual data and regression line"""
    plt.figure(figsize=(8, 5))

    # Actual data
    plt.scatter(hours, scores, label="Actual Data")

    # Regression line
    plt.plot(hours, predictions, label="Regression Line")

    plt.title("Study Hours vs Scores Prediction")
    plt.xlabel("Study Hours")
    plt.ylabel("Scores")
    plt.legend()

    plt.show()


def main():
    print("🚀 Day 9 – Prediction Project")

    # Train model
    model, hours, scores = train_model()

    # Save model
    save_model(model)

    # Load model
    model = load_model()

    print("✅ Model trained and loaded successfully!")

    # Evaluate model
    predictions = evaluate_model(model, hours, scores)

    # Predict new values
    predict_scores(model)

    # Show graph
    plot_graph(hours, scores, predictions)


if __name__ == "__main__":
    main()
