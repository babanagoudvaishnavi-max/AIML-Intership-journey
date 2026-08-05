
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# 📂 Load Dataset

df = pd.read_csv('data/dataset.csv')

# 🧹 Data Preprocessing

df_encoded = pd.get_dummies(df, drop_first=True)

# 🎯 Features & Target

X = df_encoded.drop('Attendance_Percentage', axis=1)
y = df_encoded['Attendance_Percentage']

# 🔀 Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42
)

# 🤖 Model Training

model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# 💾 Save Model

with open('models/attendance_model.pkl', 'wb') as f:
pickle.dump(model, f)

# 📈 Evaluation

y_pred = model.predict(X_test)

print("Model Performance:")
print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")
print(f"R2 Score: {r2_score(y_test, y_pred):.2f}")
