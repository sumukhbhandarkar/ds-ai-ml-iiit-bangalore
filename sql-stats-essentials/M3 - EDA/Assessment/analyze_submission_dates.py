import pandas as pd

# Read the dataset
df = pd.read_csv('../../../datasets/grades.csv')

# Convert submit_time to datetime
df['submit_time'] = pd.to_datetime(df['submit_time'])

# Extract date and count submissions by date
date_counts = df['submit_time'].dt.date.value_counts().sort_index()

print("\nSubmissions by Date Analysis:")
print("=" * 50)
print("\nAll submission dates (sorted by date):")
for date, count in date_counts.items():
    print(f"{date}: {count} submissions")

# Find the date with most submissions
peak_date = date_counts.idxmax()
peak_count = date_counts.max()
print("\nPeak Submission Date:")
print(f"{peak_date}: {peak_count} submissions")
print(f"This represents {(peak_count/len(df)*100):.2f}% of all submissions") 