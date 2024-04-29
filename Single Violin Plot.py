import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the Excel file with the specified sheet name
file_path = "/Users/qichenyuan/Desktop/NGS-117/NGS-117.xlsx"
sheet_name = "100pmol"
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Print out the column names
print(df.columns)

# Create the violin plot with statistics
plt.figure(figsize=(10, 6))
sns.violinplot(data=df['100pmol'], inner="quartile", color='#C44E52')

# Add strip plot with jitter to avoid overlapping dots
sns.stripplot(data=df['100pmol'], jitter=True, color='#FB8072', alpha=1)

# Add sample amount labels
plt.text(-0.1, df['100pmol'].max() + 0.2, f"n={len(df['100pmol'].dropna())}", ha='center')

# Calculate statistics
stats = df['100pmol'].describe()

# Add statistical labels on the left side of the violin plot
plt.text(-0.3, stats.loc['max'] + 0.2, f"Mean: {stats.loc['mean']:.2f}\nStd: {stats.loc['std']:.2f}\nMedian: {stats.loc['50%']:.2f}", ha='left')

plt.title('96-plex Base Editing with pooled SYNTHEGO gRNAs and ABE9 mRNA')
plt.xlabel('Dose of Pooled 96-plex gRNAs for each transfection')
plt.ylabel('% Perfectly Edited Allele')
plt.show()
