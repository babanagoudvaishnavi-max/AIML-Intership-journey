# =========================================
# Day 3 – NumPy Basics
# Name: Vaishnavi Babanagoud
# =========================================

import numpy as np

print("===== NUMPY BASICS PROGRAM =====\n")

# -------------------------------
# 1. Create Arrays
# -------------------------------
print("1. Array Creation")

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("1D Array:", arr1)
print("2D Array:\n", arr2)


# -------------------------------
# 2. Array Operations
# -------------------------------
print("\n2. Array Operations")

print("Addition:", arr1 + 2)
print("Multiplication:", arr1 * 2)


# -------------------------------
# 3. Indexing & Slicing
# -------------------------------
print("\n3. Indexing & Slicing")

print("First element:", arr1[0])
print("Slice (1 to 3):", arr1[1:4])


# -------------------------------
# 4. Reshaping
# -------------------------------
print("\n4. Reshaping")

reshaped = arr1.reshape(5, 1)
print("Reshaped Array:\n", reshaped)


# -------------------------------
# 5. Mathematical Operations
# -------------------------------
print("\n5. Mathematical Operations")

print("Sum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Max:", np.max(arr1))


print("\n===== PROGRAM COMPLETED SUCCESSFULLY =====")
