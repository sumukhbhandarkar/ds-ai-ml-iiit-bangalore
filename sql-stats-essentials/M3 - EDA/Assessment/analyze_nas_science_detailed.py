import pandas as pd
import numpy as np
from scipy import stats

# Read the NAS dataset
df = pd.read_csv('../../../datasets/nas.csv')

# Convert Science marks to numeric, handling any non-numeric values
df['Science..'] = pd.to_numeric(df['Science..'], errors='coerce')

# Calculate overall average science marks
overall_avg = df['Science..'].mean()
print(f"\nOverall average science marks: {overall_avg:.2f}")

# Function to perform t-test
def perform_ttest(group1, group2):
    t_stat, p_val = stats.ttest_ind(group1, group2, nan_policy='omit')
    return t_stat, p_val

# Analyze each age group
age_groups = ['12 years', '13 years', '14 years', '15 years', '16+ years']

print("\nDetailed analysis by age group:")
print("=" * 50)

for age in age_groups:
    # Get marks for this age group
    age_data = df[df['Age'] == age]
    
    # Split by father's education
    degree_marks = age_data[age_data['Father.edu'] == 'Degree & above']['Science..'].dropna()
    others_marks = age_data[age_data['Father.edu'] != 'Degree & above']['Science..'].dropna()
    
    # Calculate statistics
    degree_mean = degree_marks.mean()
    others_mean = others_marks.mean()
    
    # Perform t-test if we have enough data
    if len(degree_marks) > 1 and len(others_marks) > 1:
        t_stat, p_val = perform_ttest(degree_marks, others_marks)
        significance = "significant" if p_val < 0.05 else "not significant"
    else:
        significance = "insufficient data"
    
    print(f"\nAge group: {age}")
    print(f"Number of students with degree-holder fathers: {len(degree_marks)}")
    print(f"Number of other students: {len(others_marks)}")
    print(f"Average marks (degree-holder fathers): {degree_mean:.2f}")
    print(f"Average marks (others): {others_mean:.2f}")
    print(f"Difference: {degree_mean - others_mean:.2f}")
    print(f"Statistical significance: {significance}")

# Analyze age ranges
print("\nAnalysis by age ranges:")
print("=" * 50)

age_ranges = {
    '12-14 years': ['12 years', '13 years', '14 years'],
    '15+ years': ['15 years', '16+ years']
}

for range_name, ages in age_ranges.items():
    # Get data for this age range
    range_data = df[df['Age'].isin(ages)]
    
    # Split by father's education
    degree_marks = range_data[range_data['Father.edu'] == 'Degree & above']['Science..'].dropna()
    others_marks = range_data[range_data['Father.edu'] != 'Degree & above']['Science..'].dropna()
    
    # Calculate statistics
    degree_mean = degree_marks.mean()
    others_mean = others_marks.mean()
    
    # Perform t-test
    t_stat, p_val = perform_ttest(degree_marks, others_marks)
    significance = "significant" if p_val < 0.05 else "not significant"
    
    print(f"\nAge range: {range_name}")
    print(f"Number of students with degree-holder fathers: {len(degree_marks)}")
    print(f"Number of other students: {len(others_marks)}")
    print(f"Average marks (degree-holder fathers): {degree_mean:.2f}")
    print(f"Average marks (others): {others_mean:.2f}")
    print(f"Difference: {degree_mean - others_mean:.2f}")
    print(f"Statistical significance: {significance}")
    print(f"P-value: {p_val:.4f}") 