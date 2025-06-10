import pandas as pd
import numpy as np

# Read the dataset
df = pd.read_csv('../../../datasets/grades.csv')

# Extract filename from the submission URL (last component after the last slash)
df['filename'] = df['submission'].str.split('/').str[-1]

# Extract file extension
df['extension'] = df['filename'].str.extract(r'\.([^.]+)$', expand=False)

# Count submissions by file extension
extension_counts = df['extension'].value_counts()
extension_percentages = (extension_counts / len(df) * 100).round(2)

print("\nSubmission Format Analysis:")
print("=" * 50)
print("\nNumber of submissions by format:")
print(extension_counts)
print("\nPercentage of submissions by format:")
print(extension_percentages)

# Specifically for .zip files
zip_count = extension_counts.get('zip', 0)
zip_percentage = extension_percentages.get('zip', 0)
print(f"\nZIP file submissions:")
print(f"Count: {zip_count}")
print(f"Percentage: {zip_percentage}%") 