import pandas as pd
import numpy as np

# Read the NAS dataset
df = pd.read_csv('../../../datasets/nas.csv')

# Convert Science marks to numeric, handling any non-numeric values
df['Science..'] = pd.to_numeric(df['Science..'], errors='coerce')

# Calculate overall average science marks
overall_avg = df['Science..'].mean()
print(f"\nOverall average science marks: {overall_avg:.2f}")

# Filter for fathers with degree and above
degree_fathers = df[df['Father.edu'] == 'Degree & above']

# Group by age and calculate mean science marks for all students and those with degree fathers
age_groups = df.groupby('Age')['Science..'].agg(['mean', 'count']).round(2)
degree_age_groups = degree_fathers.groupby('Age')['Science..'].agg(['mean', 'count']).round(2)

print("\nAll students - Average science marks by age:")
print(age_groups)

print("\nStudents with degree-holder fathers - Average science marks by age:")
print(degree_age_groups)

# Calculate difference from overall average
print("\nDifference from overall average for students with degree-holder fathers:")
for age in degree_age_groups.index:
    if age != '11 years':  # Exclude 11 years age group
        diff = degree_age_groups.loc[age, 'mean'] - overall_avg
        count = degree_age_groups.loc[age, 'count']
        print(f"Age {age}: {diff:.2f} (n={count})")

# Group ages into ranges for clearer analysis
age_ranges = {
    '12-14 years': ['12 years', '13 years', '14 years'],
    '15+ years': ['15 years', '16+ years']
}

print("\nAnalysis by age ranges:")
for range_name, ages in age_ranges.items():
    range_avg = df[df['Age'].isin(ages)]['Science..'].mean()
    degree_range_avg = degree_fathers[degree_fathers['Age'].isin(ages)]['Science..'].mean()
    diff = degree_range_avg - range_avg
    n_students = len(degree_fathers[degree_fathers['Age'].isin(ages)])
    print(f"\n{range_name}:")
    print(f"Average for all students: {range_avg:.2f}")
    print(f"Average for students with degree-holder fathers: {degree_range_avg:.2f}")
    print(f"Difference: {diff:.2f}")
    print(f"Number of students with degree-holder fathers: {n_students}") 