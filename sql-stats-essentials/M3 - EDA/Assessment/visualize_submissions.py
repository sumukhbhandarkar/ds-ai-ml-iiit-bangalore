import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Read and prepare the data
df = pd.read_csv('../../../datasets/grades.csv')
df['submit_time'] = pd.to_datetime(df['submit_time'])
df['hour'] = df['submit_time'].dt.hour
df['date'] = df['submit_time'].dt.date
df['weekday'] = df['submit_time'].dt.day_name()

# Create a figure with multiple subplots
plt.figure(figsize=(15, 10))

# 1. Submissions by Hour
plt.subplot(2, 2, 1)
hour_counts = df['hour'].value_counts().sort_index()
plt.bar(hour_counts.index, hour_counts.values)
plt.title('Submissions by Hour of Day')
plt.xlabel('Hour (24-hour format)')
plt.ylabel('Number of Submissions')

# 2. Submissions by Date
plt.subplot(2, 2, 2)
date_counts = df['date'].value_counts().sort_index()
plt.bar(range(len(date_counts)), date_counts.values)
plt.title('Submissions by Date')
plt.xlabel('Date Index')
plt.ylabel('Number of Submissions')
plt.xticks(range(len(date_counts)), [d.strftime('%Y-%m-%d') for d in date_counts.index], rotation=45)

# 3. Submissions by Weekday
plt.subplot(2, 2, 3)
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_counts = df['weekday'].value_counts().reindex(weekday_order)
plt.bar(weekday_counts.index, weekday_counts.values)
plt.title('Submissions by Day of Week')
plt.xlabel('Day of Week')
plt.ylabel('Number of Submissions')
plt.xticks(rotation=45)

# 4. Cumulative Submissions Over Time
plt.subplot(2, 2, 4)
df_sorted = df.sort_values('submit_time')
cumulative_submissions = range(1, len(df) + 1)
plt.plot(df_sorted['submit_time'], cumulative_submissions)
plt.title('Cumulative Submissions Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Submissions')
plt.xticks(rotation=45)

# Adjust layout and display
plt.tight_layout()
plt.savefig('submission_patterns.png')
plt.close() 