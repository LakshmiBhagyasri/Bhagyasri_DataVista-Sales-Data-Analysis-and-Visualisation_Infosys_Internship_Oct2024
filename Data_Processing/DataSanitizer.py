import pandas as pd
import numpy as np
from scipy import stats

# Load data from a CSV file
df = pd.read_csv('data.csv')

# Inspect the data
print("Original DataFrame:")
print(df.head())
print("\nDataFrame Info:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())

# Handling Missing Values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Drop rows with any missing values (optional)
# df_cleaned = df.dropna()

# Fill missing values with a specific value (e.g., 0)
df.fillna(value=0, inplace=True)

# Removing Duplicates
print("\nNumber of Duplicate Rows:", df.duplicated().sum())
df_cleaned = df.drop_duplicates()

# Renaming Columns
df_cleaned.rename(columns={'OldName': 'NewName'}, inplace=True)

# Standardizing Text Data (only if 'text_column' exists)
if 'text_column' in df_cleaned.columns:
    df_cleaned['text_column'] = df_cleaned['text_column'].str.lower()
    df_cleaned['text_column'] = df_cleaned['text_column'].str.strip()
else:
    print("Column 'text_column' does not exist in DataFrame.")

# Outlier Detection and Removal
if 'numeric_column' in df_cleaned.columns:
    df_cleaned = df_cleaned[(np.abs(stats.zscore(df_cleaned['numeric_column'])) < 3)]
else:
    print("Column 'numeric_column' does not exist in DataFrame.")

# Final Check
print("\nCleaned DataFrame Info:")
print(df_cleaned.info())
print("\nCleaned DataFrame:")
print(df_cleaned.head())

# Export the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('cleaned_data.csv', index=False)

