# Day 7 – Machine Learning Basics

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    'Hours': [1, 2, 3, 4, 5, 6, 7, 8],
    'Scores': [35, 40, 50, 55, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

# Features & Target
X = df[['Hours']]
y = df['Scores']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model Creation
model = LinearRegression()

# Training
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Output
print("Actual Scores:", list(y_test))
print("Predicted Scores:", list(y_pred))
