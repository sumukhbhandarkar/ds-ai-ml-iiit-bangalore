import pandas as pd
import numpy as np

# Read the Excel file, skipping the first few rows that contain metadata
df = pd.read_excel('datasets/EDA_census.xlsx', skiprows=4)

# Filter for state-level data (where Unnamed: 2 is 0.0 for state-level)
# and remove rows where state name is NaN or INDIA
state_data = df[
    (df['Unnamed: 2'] == 0.0) & 
    (df['Unnamed: 3'].notna()) & 
    (df['Unnamed: 3'] != 'INDIA')
]

# Group by state and calculate total literacy rate
state_literacy = state_data.groupby('Unnamed: 3').agg({
    'Persons': 'sum',
    'Persons.2': 'sum'
}).reset_index()

# Calculate literacy rate for each state
state_literacy['Literacy_Rate'] = (state_literacy['Persons.2'] / state_literacy['Persons']) * 100

# Sort states by literacy rate
state_literacy_sorted = state_literacy.sort_values('Literacy_Rate')

# Print results
print("\nStates sorted by literacy rate (lowest to highest):")
for _, row in state_literacy_sorted.iterrows():
    print(f"{row['Unnamed: 3']}: {row['Literacy_Rate']:.2f}%") 