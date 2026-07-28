import pandas as pd

# Load the dataset
df = pd.read_csv("sample_dataset.csv")

# Display original dataset
print("Original Dataset")
print(df)

# Dataset information
print("\nDataset Information")
print(df.info())

# Check missing values
print("\nMissing Values")
print(df.isnull().sum())

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Department"] = df["Department"].fillna("Unknown")
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Remove duplicate rows
df = df.drop_duplicates()

# Display cleaned dataset
print("\nCleaned Dataset")
print(df)

# Display statistical summary
print("\nStatistical Summary")
print(df.describe())

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned dataset saved successfully!")
