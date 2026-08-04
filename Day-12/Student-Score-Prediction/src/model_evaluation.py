import pandas as pd
import pickle
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv('data/dataset.csv')

X = data[['Hours']]
y = data['Score']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Load model
with open('models/student_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("📈 Model Evaluation:")
print("MAE:", mae)
print("MSE:", mse)
print("R2 Score:", r2)
