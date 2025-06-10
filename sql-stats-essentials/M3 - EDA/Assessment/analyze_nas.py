import pandas as pd
import numpy as np

# Read the NAS dataset
df = pd.read_csv('../../../datasets/nas.csv')

# Filter for children with illiterate mothers
illiterate_mothers = df[df['Mother.edu'] == 'Illiterate']

# Count the distribution of siblings
sibling_counts = illiterate_mothers['Siblings'].value_counts().sort_index()

print("\nDistribution of siblings for children with illiterate mothers:")
print("\nAbsolute counts:")
print(sibling_counts)
print("\nPercentages:")
for siblings, percentage in (sibling_counts / len(illiterate_mothers) * 100).items():
    print(f"{siblings}: {percentage:.2f}%")

print("\nMost common number of siblings:", sibling_counts.index[sibling_counts.argmax()]) 