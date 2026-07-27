# =========================================
# Day 4 – Pandas Basics
# Name: Vaishnavi Babanagoud
# =========================================

import pandas as pd

print("===== PANDAS BASICS PROGRAM =====\n")

# -------------------------------
# 1. Create Student Dataset
# -------------------------------
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Study_Hours": [2, 3, 5, 1, 4],
    "Marks": [50, 60, 80, 40, 70]
}

df = pd.DataFrame(data)

print("📌 Student Dataset:\n")
print(df)


# -------------------------------
# 2. Explore Rows
# -------------------------------
print("\n📌 First 3 Rows:")
print(df.head(3))

print("\n📌 Last 2 Rows:")
print(df.tail(2))


# -------------------------------
# 3. Explore Columns
# -------------------------------
print("\n📌 Column Names:")
print(df.columns)

print("\n📌 Select 'Marks' Column:")
print(df["Marks"])


# -------------------------------
# 4. Dataset Information
# -------------------------------
print("\n📌 Dataset Info:")
df.info()

print("\n📌 Dataset Shape (Rows, Columns):")
print(df.shape)

print("\n📌 Statistical Summary:")
print(df.describe())


# -------------------------------
# 5. Filtering Data
# -------------------------------
print("\n📌 Students with Marks > 60:")
print(df[df["Marks"] > 60])
Give me output of this

print("\n===== PROGRAM COMPLETED SUCCESSFULLY =====") output of this 
