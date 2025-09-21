"""
Part 2: Data Cleaning and Preparation
-------------------------------------
This script cleans the dataset:
- Fills missing values with placeholders
- Converts publish_time to datetime format
- Keeps only the important columns
"""

import pandas as pd

# 1. Load dataset
df = pd.read_csv("metadata_sample.csv")

# 2. Fill missing values with "Unknown"
df.fillna("Unknown", inplace=True)

# 3. Convert publish_time column to datetime format
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")

# 4. Keep only selected useful columns
df = df[["title", "authors", "journal", "publish_time"]]

# 5. Save the cleaned dataset for later use
df.to_csv("metadata_clean.csv", index=False)

print("✅ Cleaning complete. Saved as metadata_clean.csv")
