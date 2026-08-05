# model_evaluation.py

import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import mean_absolute_error, r2_score

📂 Load Dataset

df = pd.read_csv('data/dataset.csv')

🧹 Data Preprocessing

df_encoded = pd.get_dummies(df, drop_first=True)

🎯 Features & Target

X = df_encoded.drop('Attendance_Percentage', axis=1)
y = df_encoded['Attendance_Percentage']

📦 Load Trained Model

with open('models/attendance_model.pkl', 'rb') as f:
model = pickle.load(f)

🔮 Predictions

y_pred = model.predict(X)

📈 Evaluation Metrics

mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)

print("📊 Model Evaluation Results")
print("----------------------------")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"R2 Score: {r2:.2f}")

📊 Visualization: Actual vs Predicted

plt.figure(figsize=(8,5))
sns.scatterplot(x=y, y=y_pred)
plt.xlabel("Actual Attendance")
plt.ylabel("Predicted Attendance")
plt.title("Actual vs Predicted Attendance")
plt.show()

📊 Residual Plot

residuals = y - y_pred

plt.figure(figsize=(8,5))
sns.histplot(residuals, kde=True)
plt.title("Residual Distribution")
plt.xlabel("Error")
plt.show()
