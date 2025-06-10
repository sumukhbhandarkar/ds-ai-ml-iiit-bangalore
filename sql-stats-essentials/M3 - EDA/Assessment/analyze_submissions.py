import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv('../../../datasets/grades.csv')

# Convert submit_time to datetime
df['submit_time'] = pd.to_datetime(df['submit_time'])

# Extract various time components
df['date'] = df['submit_time'].dt.date
df['year'] = df['submit_time'].dt.year
df['month'] = df['submit_time'].dt.month
df['day'] = df['submit_time'].dt.day
df['hour'] = df['submit_time'].dt.hour
df['minute'] = df['submit_time'].dt.minute
df['weekday'] = df['submit_time'].dt.day_name()

# Define deadlines
first_deadline = pd.to_datetime('2017-01-03 23:59:59')
second_deadline = pd.to_datetime('2017-01-09 23:59:59')

# Categorize submissions
df['submission_category'] = pd.cut(df['submit_time'], 
                                 bins=[df['submit_time'].min(), first_deadline, second_deadline, df['submit_time'].max()],
                                 labels=['Before First Deadline', 'Between Deadlines', 'After Second Deadline'])

# Analysis of dates
print("\nSubmission Date Analysis:")
print("=" * 50)
date_counts = df['date'].value_counts().sort_index()
print("\nSubmissions by date:")
print(date_counts)

# Analysis of submission timing relative to deadlines
print("\nSubmission Timing Analysis:")
print("=" * 50)
deadline_stats = df['submission_category'].value_counts()
print("\nSubmissions by deadline category:")
print(deadline_stats)
print("\nPercentages:")
print(deadline_stats / len(df) * 100)

# Analysis of hours
print("\nHourly Submission Analysis:")
print("=" * 50)
hour_counts = df['hour'].value_counts().sort_index()
print("\nSubmissions by hour of day:")
print(hour_counts)

# Analysis of weekdays
print("\nWeekday Analysis:")
print("=" * 50)
weekday_counts = df['weekday'].value_counts()
print("\nSubmissions by day of week:")
print(weekday_counts)

# Calculate some key statistics
print("\nKey Statistics:")
print("=" * 50)
print(f"\nTotal number of submissions: {len(df)}")
print(f"Number of unique students: {df['submission'].nunique()}")
print("\nMost popular submission times:")
print(df.groupby('hour')['submission'].count().sort_values(ascending=False).head())

# Last-minute submissions analysis (within 24 hours of deadlines)
last_minute_first = df[df['submit_time'].between(first_deadline - pd.Timedelta(days=1), first_deadline)]
last_minute_second = df[df['submit_time'].between(second_deadline - pd.Timedelta(days=1), second_deadline)]

print("\nLast-minute Submission Analysis:")
print("=" * 50)
print(f"\nSubmissions in last 24 hours before first deadline: {len(last_minute_first)}")
print(f"Submissions in last 24 hours before second deadline: {len(last_minute_second)}")

# Calculate average submission time (hour of day)
avg_hour = df['hour'].mean()
print(f"\nAverage submission hour: {avg_hour:.2f} (24-hour format)")

# Most common submission patterns
print("\nMost Common Submission Patterns:")
print("=" * 50)
print("\nMost common hours:")
print(df['hour'].value_counts().head())
print("\nMost common dates:")
print(df['date'].value_counts().head()) 