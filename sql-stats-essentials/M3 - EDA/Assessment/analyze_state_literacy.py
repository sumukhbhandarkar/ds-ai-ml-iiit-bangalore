import pandas as pd
import numpy as np

# Read the Excel file
df = pd.read_excel('datasets/EDA_census.xlsx', skiprows=4)

# Get state-level data (where district code is 0 and area name is not INDIA)
# Also filter for 'All ages' to get total population
state_data = df[
    (df['Unnamed: 2'] == 0) & 
    (df['Unnamed: 3'] != 'INDIA') & 
    (df['Unnamed: 5'] == 'All ages')
]

# Function to calculate female literacy rate
def calculate_female_literacy_rate(row):
    total_females = float(row['Females'])
    literate_females = float(row['Females.2'])
    return (literate_females/total_females)*100 if total_females > 0 else 0

# Calculate literacy rates for each state
state_literacy = []

for _, row in state_data.iterrows():
    if pd.notna(row['Unnamed: 3']):  # Check if state name exists
        state_name = row['Unnamed: 3'].strip()
        literacy_rate = calculate_female_literacy_rate(row)
        state_literacy.append({'State': state_name, 'Female_Literacy_Rate': literacy_rate})

# Convert to DataFrame, remove duplicates, and sort by literacy rate
results_df = pd.DataFrame(state_literacy)
results_df = results_df.sort_values('Female_Literacy_Rate', ascending=False)

# Display results
print("\nFemale Literacy Rates by State:")
print("-" * 50)
for _, row in results_df.iterrows():
    print(f"{row['State']:<30} : {row['Female_Literacy_Rate']:.2f}%")

# Display the highest literacy rate
highest = results_df.iloc[0]
print(f"\nHighest female literacy rate: {highest['State']} ({highest['Female_Literacy_Rate']:.2f}%)") 