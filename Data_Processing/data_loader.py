import pandas as pd

# Load only the header row from the CSV
df = pd.read_csv('data.csv', nrows=0)

# Extract the headings
headings = df.columns.tolist()

# Print the headings
print("Headings:", headings)