import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'OldName1': [1, 2, 3],
    'OldName2': [4, 5, 6],
    'OldName3': [7, 8, 9]
})

# Print original DataFrame
print("Original DataFrame:")
print(df)

# Rename all columns
df.columns = ['NewName1', 'NewName2', 'NewName3']

# Print updated DataFrame
print("\nDataFrame after renaming all columns:")
print(df)