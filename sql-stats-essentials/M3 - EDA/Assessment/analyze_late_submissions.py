import pandas as pd
from datetime import datetime

# Read the dataset
df = pd.read_csv('../../../datasets/grades.csv')

# Convert submit_time to datetime
df['submit_time'] = pd.to_datetime(df['submit_time'])

# Define deadlines
first_deadline = pd.to_datetime('2017-01-03 23:59:59')
second_deadline = pd.to_datetime('2017-01-09 23:59:59')

# Count submissions after first deadline
late_submissions = df[df['submit_time'] > first_deadline]
after_second_deadline = df[df['submit_time'] > second_deadline]

print("\nLate Submission Analysis:")
print("=" * 50)
print(f"\nTotal submissions: {len(df)}")
print(f"Submissions after first deadline: {len(late_submissions)}")
print(f"Percentage of late submissions: {(len(late_submissions) / len(df) * 100):.2f}%")

print("\nBreakdown of late submissions:")
print(f"Between first and second deadline: {len(late_submissions) - len(after_second_deadline)}")
print(f"After second deadline: {len(after_second_deadline)}")

# Show the dates of late submissions
print("\nDates of late submissions:")
late_dates = late_submissions['submit_time'].dt.date.value_counts().sort_index()
print(late_dates) 