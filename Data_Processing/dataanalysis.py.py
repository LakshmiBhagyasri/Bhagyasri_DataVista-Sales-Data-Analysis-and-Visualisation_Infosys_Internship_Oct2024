import pandas as pd

# Load the CSV file
df = pd.read_csv('data.csv')

# Extract the headings (column names)
headings = df.columns.tolist()

# Print the headings
print("Headings:", headings)