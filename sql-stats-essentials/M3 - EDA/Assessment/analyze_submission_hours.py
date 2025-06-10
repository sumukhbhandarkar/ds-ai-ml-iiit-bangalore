import pandas as pd

# Read the dataset
df = pd.read_csv('../../../datasets/grades.csv')

# Convert submit_time to datetime
df['submit_time'] = pd.to_datetime(df['submit_time'])

# Extract hour and count submissions by hour
hour_counts = df['submit_time'].dt.hour.value_counts().sort_index()

print("\nSubmissions by Hour Analysis:")
print("=" * 50)
print("\nAll submission hours (24-hour format):")
for hour, count in hour_counts.items():
    # Convert 24-hour format to 12-hour format for better readability
    if hour == 0:
        hour_12 = "12 AM"
    elif hour < 12:
        hour_12 = f"{hour} AM"
    elif hour == 12:
        hour_12 = "12 PM"
    else:
        hour_12 = f"{hour-12} PM"
    
    print(f"{hour:02d}:00 ({hour_12}): {count} submissions")

# Find the hour with most submissions
peak_hour = hour_counts.idxmax()
peak_count = hour_counts.max()

# Convert peak hour to 12-hour format
if peak_hour == 0:
    peak_hour_12 = "12 AM"
elif peak_hour < 12:
    peak_hour_12 = f"{peak_hour} AM"
elif peak_hour == 12:
    peak_hour_12 = "12 PM"
else:
    peak_hour_12 = f"{peak_hour-12} PM"

print("\nPeak Submission Hour:")
print(f"{peak_hour:02d}:00 ({peak_hour_12}): {peak_count} submissions")
print(f"This represents {(peak_count/len(df)*100):.2f}% of all submissions")

# Show top 5 busiest hours
print("\nTop 5 Busiest Hours:")
top_5_hours = hour_counts.nlargest(5)
for hour, count in top_5_hours.items():
    if hour == 0:
        hour_12 = "12 AM"
    elif hour < 12:
        hour_12 = f"{hour} AM"
    elif hour == 12:
        hour_12 = "12 PM"
    else:
        hour_12 = f"{hour-12} PM"
    print(f"{hour:02d}:00 ({hour_12}): {count} submissions ({(count/len(df)*100):.2f}%)") 