import pandas as pd

# Load the CSV data
data = pd.read_csv('form_data.csv')

# Display first few entries
print(data.head())

# Example: Count how many people have submitted the form
print(f"Total submissions: {len(data)}")

# Example: Display unique email count
print(f"Unique email addresses: {data['email'].nunique()}")
