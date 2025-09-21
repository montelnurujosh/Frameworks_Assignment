"""
Part 1: Data Loading and Basic Exploration
------------------------------------------
This script loads the metadata_sample.csv file and explores its structure.
"""

import pandas as pd

# 1. Load the dataset
df = pd.read_csv("metadata_sample.csv")

# 2. Show the first few rows
print("📌 First 5 rows of the dataset:")
print(df.head(), "\n")

# 3. Dataset dimensions
print("📌 Dataset dimensions (rows, columns):")
print(df.shape, "\n")

# 4. Data types of each column
print("📌 Data types of each column:")
print(df.dtypes, "\n")

# 5. Missing values
print("📌 Missing values per column:")
print(df.isnull().sum(), "\n")

# 6. Basic statistics
print("📌 Basic statistics for all columns:")
print(df.describe(include="all"))
